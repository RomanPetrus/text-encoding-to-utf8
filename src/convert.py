# imports
from pathlib import Path
from charset_normalizer import detect

# config
PROJECT_DIR = Path(__file__).resolve().parents[1]

raw_dir = PROJECT_DIR / "data_raw"
out_dir = PROJECT_DIR / "data_utf8"
out_dir.mkdir(exist_ok=True)

# functions
def read_file(file_name: str, path_dir: Path) -> bytes: 
    """
    Read a file from disk as raw bytes.
    """
    file_path = path_dir / file_name
    if not file_path.is_file():
        raise FileNotFoundError(f"{file_path.name} is not a file")
        
    data = file_path.read_bytes()
    print(file_path.name, "bytes:", len(data))        
    return data

def guess_encoding(data: bytes) -> str:
    """
    Guess the character encoding of raw byte data.
    """
    result = detect(data)
    enc = result.get("encoding")    
    print(f"Detected encoding: {enc}, confidence: {result.get('confidence')}")
    return enc

def decode_bytes(data: bytes, encoding: str="utf-8") -> str:
    """
     Decode raw bytes into a Unicode string using the given encoding.
    """
    text = data.decode(encoding, errors="strict")
    return text

def save_utf8(text: str, file_name: str, out_dir: Path) -> Path:
    """
    Save decoded text to a UTF-8 encoded file.
    """
    out_path = out_dir / f"utf8_{file_name}"
    out_path.write_text(text, encoding = "utf-8")
    return out_path

def main() -> None:
    files_names = sorted([file.name for file in raw_dir.iterdir()])
    for name in files_names:
        data = read_file(name, raw_dir)
        enc = guess_encoding(data)
        text = decode_bytes(data, enc)
        save_utf8(text, name, out_dir)
if __name__ == "__main__":
    main()



