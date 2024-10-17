from hash_utils import HASH_FUNCTIONS
from file_manager import load_file_hashes, get_file_size
import os

def verify_file_integrity(file_path: str) -> str:
    file_hashes = load_file_hashes()
    file_name = os.path.basename(file_path)
    
    if file_name not in file_hashes:
        return f"File '{file_name}' not found. Please upload the file first."

    stored_hash = file_hashes[file_name]
    current_size = get_file_size(file_path)
    
    # Calculate all current hashes
    current_hashes = {
        name: func(file_path) 
        for name, func in HASH_FUNCTIONS.items()
    }
    
    # Check file size
    size_match = stored_hash.get("size") == current_size
    
    # Prepare results for each hash algorithm
    results = []
    all_passed = True
    
    # Add size check result
    results.append(f"File Size: {'Passed' if size_match else 'Failed'}")
    if not size_match:
        all_passed = False
    
    # Check each hash algorithm
    for algorithm in HASH_FUNCTIONS.keys():
        if algorithm in stored_hash:
            hash_match = stored_hash[algorithm] == current_hashes[algorithm]
            results.append(f"{algorithm.upper()}: {'Passed' if hash_match else 'Failed'}")
            if not hash_match:
                all_passed = False
    
    # Prepare the final output
    header = f"File '{file_name}' verified {'successfully' if all_passed else 'with failures'}."
    tests_results = "\n".join(results)
    
    return f"{header}\nTests: \n{tests_results}"