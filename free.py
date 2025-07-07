import os
import shutil
import getpass

def clean_directory(path):
    if os.path.exists(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"Failed to delete {item_path}: {e}")

# Get username for prefetch path
username = getpass.getuser()

# Define paths
temp_path = os.getenv('TEMP')
windows_temp_path = r"C:\Windows\Temp"
prefetch_path = r"C:\Windows\prefetch"

# Clean each directory
print("Cleaning TEMP folder...")
clean_directory(temp_path)

print("Cleaning C:\\Windows\\Temp...")
clean_directory(windows_temp_path)

print("Cleaning Prefetch folder...")
clean_directory(prefetch_path)

print("Cleanup complete.")