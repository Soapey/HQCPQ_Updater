import urllib.request
import configparser
import os
import sys

def resource_path(relative_path):

    base_path = os.path.abspath(".")

    full_path = os.path.join(base_path, relative_path)

    return full_path


def read_config():
    config = configparser.ConfigParser()
    config.read(resource_path(r"files\config.ini"))
    return config


def main():
    
    config = read_config()
    
    download_link = config['AppSettings']['update_file_url']
    save_to_path = os.path.join(os.path.abspath("."), "HQCPQ.exe")

    if os.path.exists(save_to_path):
        os.remove(save_to_path)

    print("Starting download.")
    filename, headers = urllib.request.urlretrieve(download_link, save_to_path)

    sys.exit()

if __name__ == "__main__":
    main()