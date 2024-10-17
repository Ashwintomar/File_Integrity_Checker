import hashlib
import zlib
import blake3
from typing import Callable, Dict

def calculate_sha256(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def calculate_crc32(file_path: str) -> str:
    prev = 0
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            prev = zlib.crc32(byte_block, prev)
    return f"{prev & 0xFFFFFFFF:08x}"

def calculate_md5(file_path: str) -> str:
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def calculate_sha1(file_path: str) -> str:
    sha1_hash = hashlib.sha1()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha1_hash.update(byte_block)
    return sha1_hash.hexdigest()

def calculate_sha3_256(file_path: str) -> str:
    sha3_hash = hashlib.sha3_256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha3_hash.update(byte_block)
    return sha3_hash.hexdigest()

def calculate_blake3(file_path: str) -> str:
    blake3_hash = blake3.blake3()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            blake3_hash.update(byte_block)
    return blake3_hash.hexdigest()

def calculate_adler32(file_path: str) -> str:
    prev = 1  # Adler-32 starts with 1
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            prev = zlib.adler32(byte_block, prev)
    return f"{prev & 0xFFFFFFFF:08x}"

# Dictionary mapping algorithm names to their functions
HASH_FUNCTIONS: Dict[str, Callable[[str], str]] = {
    "sha256": calculate_sha256,
    "crc32": calculate_crc32,
    "md5": calculate_md5,
    "sha1": calculate_sha1,
    "sha3_256": calculate_sha3_256,
    "blake3": calculate_blake3,
    "adler32": calculate_adler32
}