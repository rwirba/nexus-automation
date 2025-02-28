import requests
import os

NEXUS_URL = "http://nexus.kihhuf.org:8081/repository/infra"
USERNAME = "admin"
PASSWORD = "admin"

def upload_file(filepath, destination_path):
    with open(filepath, "rb") as f:
        response = requests.put(f"{NEXUS_URL}/{destination_path}", auth=(USERNAME, PASSWORD), data=f)
        if response.status_code == 201:
            print(f"Uploaded {filepath} to {destination_path}")
        else:
            print(f"Failed to upload {filepath}: {response.text}")

def move_old_version(os_type, app, version):
    old_version_path = f"{os_type}/{app}/{version}/"
    current_path = f"{os_type}/{app}/current/"

    # Move existing current files to versioned folder
    os.makedirs(old_version_path, exist_ok=True)
    for file in os.listdir(current_path):
        os.rename(f"{current_path}/{file}", f"{old_version_path}/{file}")

def upload_new_version(os_type, app, version):
    new_files = os.listdir("downloads/")
    
    for file in new_files:
        upload_file(f"downloads/{file}", f"{os_type}/{app}/current/{file}")

# Example usage
move_old_version("ubuntu", "splunk", "1.2.1")
upload_new_version("ubuntu", "splunk", "1.3.0")  # Assuming 1.3.0 is the new version
