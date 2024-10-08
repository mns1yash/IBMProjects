import os

# Directory structure for the Student Event Page project
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

# Function to create directories
def create_directories(base_folder, structure):
    try:
        # Create base folder if it doesn't exist
        for folder, subfolders in structure.items():
            base_path = os.path.join(base_folder, folder)
            os.makedirs(base_path, exist_ok=True)
            print(f"Created base folder: {base_path}")

            # Create subdirectories inside the base folder
            for subfolder in subfolders:
                subfolder_path = os.path.join(base_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                print(f"Created subfolder: {subfolder_path}")
    except Exception as e:
        print(f"Error creating directories: {e}")

# Define the base folder path (/mnt/data for example, or use a local path)
base_path = '/mnt/data'

# Create the folder structure
create_directories(base_path, folder_structure)

# List the created structure
print("\nDirectory structure created under:", base_path)
for root, dirs, files in os.walk(os.path.join(base_path, 'StudentEventPage')):
    level = root.replace(os.path.join(base_path, 'StudentEventPage'), '').count(os.sep)
    indent = ' ' * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 4 * (level + 1)
    for d in dirs:
        print(f"{sub_indent}{d}/")
