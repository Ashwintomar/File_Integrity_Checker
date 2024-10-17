import os
import json
from typing import Dict

HASH_FILE = "file_hashes.json"

def load_file_hashes() -> Dict[str, Dict]:
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_file_hashes(file_hashes: Dict[str, Dict]):
    with open(HASH_FILE, "w") as f:
        json.dump(file_hashes, f, indent=2)

def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)

def create_hash_result(file_hashes: Dict[str, str], algorithm: str) -> str:
    return f"{algorithm.upper()}: {file_hashes[algorithm]}"