# File Integrity Checker

This is a Python-based application to verify the integrity of files using multiple hashing algorithms. The application is built using **Gradio** for the user interface, making it easy to upload files, verify their integrity, and list all files in the system.

## Features

- **File Upload**: Upload multiple files and calculate their hashes using various algorithms.
- **File Verification**: Check the integrity of a file by comparing its stored and current hashes and file size.
- **List Files**: View all files uploaded to the system along with their size and hash details.
- **Multiple Hashing Methods**: Includes seven different hash algorithms for comprehensive file integrity checks:
  - SHA-256 (Secure Hash Algorithm 256-bit)
  - CRC32 (Cyclic Redundancy Check 32-bit)
  - MD5 (Message Digest Algorithm 5)
  - SHA-1 (Secure Hash Algorithm 1)
  - SHA3-256 (Secure Hash Algorithm 3 256-bit)
  - BLAKE3 (Modern cryptographic hash function)
  - Adler-32 (Rolling hash function)

## Requirements

Make sure you have **Python 3.7+** installed. You can install the required packages using `pip`.

### Required Python Libraries:
- `gradio`: For building the web interface
- `blake3`: For BLAKE3 hash computation
- `hashlib`: For various hash algorithms (SHA-256, MD5, SHA-1, SHA3-256)
- `zlib`: For CRC32 and Adler-32 checksums
- `typing`: For type hints
- Standard libraries: `os`, `json`

You can install these dependencies using:
```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Ashwintomar/File_Integrity_Checker.git
cd File_Integrity_Checker
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Once all dependencies are installed, you can run the application using:
```bash
python main.py
```

This will launch the **Gradio** interface in your browser, where you can interact with the application.

## Usage

1. **Upload Files**: Navigate to the "Upload Files" tab, select files from your computer, and click "Upload and Calculate Hash". The system will calculate and store all supported hashes for each file.

2. **Verify File Integrity**: Go to the "Verify File" tab, select a file, and click "Verify File Integrity". The system will check if the file's current hashes match the stored values.

3. **List All Files**: In the "List Files" tab, click the "List All Files" button to view all the files in the system, including their size and hash details.

## File Structure

The application is modular and consists of the following files:

```text
- main.py            # Main Gradio interface for running the app
- hash_utils.py      # Utility functions for calculating file hashes
- file_manager.py    # Functions for loading/saving file metadata
- verify_file.py     # Logic for verifying file integrity
- requirements.txt   # Required Python packages
```

### `main.py`
This is the main script that initializes the Gradio interface. It uses the functions from the other files to upload, verify, and list files.

### `hash_utils.py`
This file contains functions to calculate various hashes for the files:
- SHA-256, CRC32, MD5, SHA-1, SHA3-256, BLAKE3, and Adler-32 hash functions
- Central hash function registry for easy extension

### `file_manager.py`
Handles file management, including loading and saving file hashes and metadata:
- `load_file_hashes`: Loads file metadata from a JSON file
- `save_file_hashes`: Saves file metadata to a JSON file
- `get_file_size`: Retrieves the file size

### `verify_file.py`
Handles file integrity verification:
- Verifies the integrity of a file by comparing all stored and current hashes
- Provides detailed test results for each hash algorithm

## Example Output

### Upload Files
```
File: example.txt
SHA256: abcdef123456...
CRC32: 89abcd12
MD5: 123456789abc...
SHA1: def987654321...
SHA3_256: 456789abcdef...
BLAKE3: 789abcdef123...
ADLER32: bcdef12345...
```

### Verify File
```
File 'example.txt' verified successfully.
Tests:
File Size: Passed
SHA256: Passed
CRC32: Passed
MD5: Passed
SHA1: Passed
SHA3_256: Passed
BLAKE3: Passed
ADLER32: Passed
```

### List Files
```
File: example.txt (1024 bytes)
SHA256: abcdef123456...
CRC32: 89abcd12
MD5: 123456789abc...
SHA1: def987654321...
SHA3_256: 456789abcdef...
BLAKE3: 789abcdef123...
ADLER32: bcdef12345...
```

## Contribution

Feel free to fork this repository and submit pull requests. For major changes, please open an issue to discuss what you would like to change.
