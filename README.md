# Detecting and Converting Text Encodings to UTF-8

This project demonstrates a complete, byte-safe pipeline for detecting
character encodings and converting heterogeneous text files into clean UTF-8.

The focus is on **robust handling of mixed encodings**, safe decoding,
and reproducible normalization of raw text data — a common real-world
data engineering problem.

## Results

- All input files with different original encodings were successfully read
- Character encodings were detected automatically
- Text was decoded safely using strict decoding with fallbacks
- All files were saved as valid UTF-8 outputs
- No data loss for correctly decoded files



## Project structure

text-encoding-to-utf8/
│
├─ notebooks/
│ └─ encoding_lab.ipynb
│
├─ src/
│ └─ convert.py
│
├─ data_raw/
│ └─ original input files
│
├─ data_utf8/
│ └─ converted UTF-8 files
│
├─ README.txt
├─ README.md
├─ requirements.txt
└─ .gitignore


## How to run

### Notebook

Open the following notebook to explore the full workflow:

- `notebooks/encoding_lab.ipynb`


### Script

Run the conversion script from the project root:

```bash

python -m src.convert

```
This reads all files from data_raw/ and writes UTF-8 outputs to data_utf8/.


### Dataset

die_ISO-8859-1.txt
file_guide.csv
harpers_ASCII.txt
olaf_Windows-1251.txt
portugal_ISO-8859-1.txt
shisei_UTF-8.txt
yan_BIG-5.txt


### Techniques used

Byte-level file reading (Path.read_bytes)
Encoding detection with charset-normalizer
Strict decoding with controlled fallbacks
UTF-8 normalization
Safe filesystem handling using pathlib
Reproducible notebook and script workflow


### Outputs

utf8_die_ISO-8859-1.txt
utf8_file_guide.csv
utf8_harpers_ASCII.txt
utf8_olaf_Windows-1251.txt
utf8_portugal_ISO-8859-1.txt
utf8_shisei_UTF-8.txt
utf8_yan_BIG-5.txt

### Notes
Encoding detection is probabilistic and validated through strict decoding
The pipeline prioritizes correctness over silent data corruption
The project is intentionally kept simple and transparent for learning purposes


