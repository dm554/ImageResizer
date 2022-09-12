import os.path as Path


# Verifies that a file exists at ../images/
def VerifyFileExists(file_name):
    file_path = "../images/" + file_name
    file_exists = Path.exists(file_path)
    if file_exists:
        print("File Found")
        return file_path
    else:
        print("File NOT Found")
        exit()
