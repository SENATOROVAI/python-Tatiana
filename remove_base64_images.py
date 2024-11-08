import re
import os

def remove_base64_images_from_file(py_file):
    with open(py_file, 'r') as f:
        content = f.read()
    
    # Regular expression to match base64 image URIs in the form of: ![image](data:image/png;base64,...)
    content_cleaned = re.sub(r'!\[.*?\]\(data:image.*?;base64,.*?\)', '', content)
    
    with open(py_file, 'w') as f:
        f.write(content_cleaned)

def remove_base64_images_from_directory(directory):
    # Iterate through all Python files in the repository
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            py_file = os.path.join(directory, filename)
            remove_base64_images_from_file(py_file)

# Run the cleanup for the current directory
remove_base64_images_from_directory('.')
