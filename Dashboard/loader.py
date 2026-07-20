from pathlib import Path
import json
import pandas as pd

DATA_FILE = Path(__file__).resolve().parent.parent / "SpendSense" / "data.json"
def load_transactions():
    with open(DATA_FILE, "r") as file:
        transactions = json.load(file)

    return pd.DataFrame(transactions)