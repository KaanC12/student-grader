import os
import pandas as pd
import secrets
from student_grader.exceptions import EmptyDatabaseError


FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(FOLDER_PATH, "..", "data", "clients.csv")

# Error Message
DATABASE_IS_EMPTY = "The database is empty."

def generate_api_key():
    return secrets.token_hex(32)

def save_key(client_name):
    if not os.path.exists(KEY_PATH) or os.path.getsize(KEY_PATH) == 0:
       key = generate_api_key()
       user = {
           "client_name": client_name,
           "api_key": key,
           "active": False
       } 

       df = pd.DataFrame([user])
       df.to_csv(KEY_PATH)

    else:
        key = generate_api_key()
        df = pd.read_csv(KEY_PATH)
        df.loc[len(df)] = {
            "client_name": client_name,
            "api_key": key,
            "active": False
        }

def check_key(api_key: str, name: str) -> bool:
    if not os.path.exists(KEY_PATH) or os.path.getsize(KEY_PATH) == 0:
        raise EmptyDatabaseError(DATABASE_IS_EMPTY)
    
    df = pd.read_csv(KEY_PATH, index_col="api_key")

    if api_key not in df.index:
        return False

    client_name = df.loc[api_key, "client_name"]

    if client_name != name:
        return False

    df.loc[api_key, "activate"] = True

    df.to_csv(KEY_PATH) 

    return bool(df.loc[api_key, "active"])
