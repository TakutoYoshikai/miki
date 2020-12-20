import zipfile
import os
import sys

def hide(office_filepath, secret_filepath):
    with zipfile.ZipFile(office_filepath, "a", zipfile.ZIP_STORED) as zf:
        zf.write(secret_filepath, os.path.basename(secret_filepath))

def main():
    hide(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
