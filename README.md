# mark-extra-phrase

A Python utility for inserting or marking `extra-phrases` in text.

---

## Features
- Insert custom phrases into text.
- Regex-based phrase detection.
- Easy to extend and test.

---

# Installation

Clone the repository and set up a virtual environment:

```
git clone https://github.com/alok1304/mark-extra-phrase.git
cd mark-extra-phrase
```
Create and activate virtual environment
```
python -m venv venv
```
On Linux/macOS
```
source venv/bin/activate
```
On Windows (PowerShell)
```
.\venv\Scripts\Activate.ps1
```

Install dependencies
```
pip install -r requirements.txt
```
        
Running Tests
Run tests using pytest:
```
python -m pytest -v tests/
```

# Usages 
After cloning this repository, you can mark extra phrases in any file or folder by running:
```
py mark-extra-phrase/src/insert_phrase.py /path/to/file-or-folder
```
# Example
```
py mark-extra-phrase/src/insert_phrase.py src/licensedcode/data/rules
```
