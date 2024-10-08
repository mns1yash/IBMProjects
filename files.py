import os
import subprocess

# Function to run shell commands and check installations
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {command}\n{e}")

# Function to check installations for all frameworks
def install_all_frameworks():
    print("Starting installations for all frameworks and prerequisites...")

    # Node.js, npm, React, Angular, Vue CLI installation
    run_command("npm install -g @angular/cli")
    run_command("npm install -g @vue/cli")
    run_command("npx create-react-app react-app")
    
    # Python and Flask, Django installations
    run_command("pip install Flask")
    run_command("pip install Django mysqlclient")
    
    # MongoDB installation
    run_command("npm install mongoose")
    
    # MySQL installation setup (ensure you have MySQL installed manually)
    run_command("pip install flask-mysqldb")
    
    print("All installations completed successfully!")

# Define the folder structure and files to be created
folder_structure = {
    'StudentEventPage': {
        'frontend': {
            'react-app': {
                'src': ['App.js', 'components/HomePage.js'],
                'public': ['index.html'],
            },
            'angular-app': {
                'src/app': ['tech-event/tech-event.component.ts'],
                'src': ['index.html'],
            },
            'vue-app': {
                'src/components': ['FoodSportsPage.vue'],
                'public': ['index.html'],
            },
            'styles': ['style.css', 'tailwind.css', 'bootstrap.css'],
        },
        'backend': {
            'node-express-api': ['app.js', 'routes/events.js'],
            'flask-api': ['app.py'],
            'django-api': {
                'events': ['models.py', 'views.py', 'urls.py'],
                'project': ['settings.py', 'urls.py'],
            },
        },
        'database': {
            'mysql': ['mysql_setup.sql'],
            'mongodb': ['mongodb_setup.txt'],
        },
        'auth': ['jwt_auth.js', 'token_auth.py', 'django_auth.py'],
        'deployment': ['heroku_setup.md', 'dockerfile'],
        'git': ['.gitignore', 'README.md'],
    }
}

# Create directories and files
def create_structure(base_folder, structure):
    for folder, content in structure.items():
        folder_path = os.path.join(base_folder, folder)
        if isinstance(content, dict):
            os.makedirs(folder_path, exist_ok=True)
            create_structure(folder_path, content)
        elif isinstance(content, list):
            os.makedirs(folder_path, exist_ok=True)
            for file in content:
                open(os.path.join(folder_path, file), 'w').close()

# Get current working directory
current_dir = os.getcwd()

# Start installations
install_all_frameworks()

# Start creating folder structure and files
create_structure(current_dir, folder_structure)
print(f"Project completed successfully in {current_dir}")
print(f"Project structure and installations completed successfully in {current_dir}")
