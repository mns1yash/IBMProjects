 
import os

# Directory structure
folder_structure = {
    'StudentEventPage': [
        'frontend/react-app',
        'frontend/angular-app',
        'frontend/vue-app',
        'frontend/styles',
        'backend/node-express-api',
        'backend/flask-api',
        'backend/django-api',
        'database/mysql',
        'database/mongodb',
        'auth',
        'deployment',
        'git'
    ]
}

# Create directories using os
def create_directories(base_folder, structure):
    for folder, subfolders in structure.items():
        base_path = os.path.join('/mnt/data', folder)  # Create under the working directory /mnt/data
        os.makedirs(base_path, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(base_path, subfolder), exist_ok=True)

# Create the folder structure
create_directories('/mnt/data', folder_structure)

# List the created structure
for root, dirs, files in os.walk('/mnt/data/StudentEventPage'):
    print(root)  # List created directories

