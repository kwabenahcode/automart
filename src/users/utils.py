import os
from os.path import join

def user_photo_directory_path(instance, filename):
    username = instance.username
    filename_without_extension = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1]
    
    # Combine username, filename without extension, and original extension
    final_filename = '{0}_{1}{2}'.format(username, filename_without_extension, extension)
    
    # Join the username folder and final filename
    return join(username, final_filename)

