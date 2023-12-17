import os
from os.path import join

def user_photo_directory_path(instance, filename):
    username = instance.username
    filename = os.path.splitext(filename)[0]  # Extract filename without extension
    extension = os.path.splitext(filename)[1]  # Get the extension
    return join(username, filename + extension)