import requests
import os

NEXUS_URL = "http://nexus.kihhuf.org:8081/repository/infra"
APPLICATIONS = ["splunk"]  # Add more applications if needed
OS_TYPES = ["ubuntu", "windows"]

def get_current_version(os_type, app_name):
    version_file = f"{NEXUS_URL}/{os_type}/{app_name}/current/version.txt"
    response = requests.get(version_file)
    
    if response.status_code == 200:
        return response.text.strip()
    return None

def check_for_updates():
    updates = {}
    
    for os_type in OS_TYPES:
        for app in APPLICATIONS:
            current_version = get_current_version(os_type, app)
            latest_version = fetch_latest_version(app)  # Implement this function
            
            if latest_version and latest_version != current_version:
                updates[f"{os_type}/{app}"] = latest_version
    
    return updates

updates = check_for_updates()
print("Updates found:", updates)
