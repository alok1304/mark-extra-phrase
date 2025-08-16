import sys
import os
import re

def replace_between(text, patterns, extra_phrase="[[6]]"):
    """
    Replace text between markers according to rules:
    1. If `extra_phrase` already present then do nothing
    2. If empty then insert `extra_phrase`
    3. If words present then replace with `extra_phrase`
    """
    for pattern in patterns:
        def repl(match):
            middle = match.group(2).strip()
            if middle == extra_phrase:  
                return match.group(1) + middle + match.group(3)
            elif not middle:  
                return match.group(1) + extra_phrase + match.group(3)
            else:  
                return match.group(1) + extra_phrase + match.group(3)
        text = pattern.sub(repl, text)
    return text

def process_file(file_path, patterns, extra_phrase="[[6]]"):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    updated_content = replace_between(content, patterns, extra_phrase)

    if updated_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"[Added extra-phrase] Updated: {file_path}")
    else:
        print(f"No changes: {file_path}")

def run_tool(target_path, patterns, extra_phrase="[[6]]"):
    """Process a file or all files inside a folder recursively."""
    if os.path.isfile(target_path):
        process_file(target_path, patterns, extra_phrase)
    elif os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                process_file(file_path, patterns, extra_phrase)
    else:
        print("Path does not exist!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/insert_phrase.py /path/to/file-or-folder")
    else:
        # define start and end markers
        patterns = [
            re.compile(r"(Neither the name of )(.*?)( nor the)", re.IGNORECASE)
        ]
        run_tool(sys.argv[1], patterns, extra_phrase="[[6]]")
