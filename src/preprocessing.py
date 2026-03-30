#Here we  data load
        # label convert
        # encoding
        # scaling
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess():
    # 🔹 Step 1: Load dataset
    df = pd.read_csv("data/KDDTrain+.txt", header=None)

    # 🔹 Step 2: Assign column names
    columns = ["duration","protocol_type","service","flag","src_bytes","dst_bytes",
           "land","wrong_fragment","urgent","hot","num_failed_logins",
           "logged_in","num_compromised","root_shell","su_attempted",
           "num_root","num_file_creations","num_shells","num_access_files",
           "num_outbound_cmds","is_host_login","is_guest_login","count",
           "srv_count","serror_rate","srv_serror_rate","rerror_rate",
           "srv_rerror_rate","same_srv_rate","diff_srv_rate",
           "srv_diff_host_rate","dst_host_count","dst_host_srv_count",
           "dst_host_same_srv_rate","dst_host_diff_srv_rate",
           "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate",
           "dst_host_serror_rate","dst_host_srv_serror_rate",
           "dst_host_rerror_rate","dst_host_srv_rerror_rate",
           "label", "difficulty"]

    df.columns = columns
    df.drop("difficulty", axis=1, inplace=True)
    # 🔹 Step 3: Convert label (normal = 0, attack = 1)
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

    # 🔹 Step 4: Encode categorical columns
    categorical_cols = ['protocol_type', 'service', 'flag']
    le = LabelEncoder()

    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # 🔹 Step 5: Split features and target
    X = df.drop('label', axis=1)
    y = df['label']

    # 🔹 Step 6: Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    # 🔹 Step 7: Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 🔹 Step 8: Return processed data
    return X_train, X_test, y_train, y_test
