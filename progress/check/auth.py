import os
import pandas as pd

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_PATH, "..", "..", "student_grader", "data", "client.csv")

def check_api_key(api_key, name):
    if not os.path.exists(KEY_PATH) or os.path.getsize(KEY_PATH) == 0:
        return False
    
    df = pd.read_csv(KEY_PATH, index_col="api_key")

    if api_key not in df.index:
        return False
    
    if df.loc[api_key, "client_name"] != name:
        return False
    
    df.loc[api_key, "active"] = True
    df.to_csv(KEY_PATH)
    return True
