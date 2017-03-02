def do():
    import setup_utilities
    setup_utilities.log("Installing avro python....")
    import os
    download_link = "http://apache.lauf-forum.at/avro/stable/py/avro-1.8.1.tar.gz"
    temp_folder = ".temp"
    temp_location = os.path.join(temp_folder, "avro.tar")
    temp_extracted_folder = os.path.join(temp_folder, "avro-1.8.1")

    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    import subprocess
    subprocess.call(["curl", download_link, "--create-dirs", "-o", temp_location])

    import shutil

    import tarfile
    tar = tarfile.open(temp_location)
    tar.extractall(path=temp_folder)
    tar.close()

    print temp_extracted_folder
    os.chdir(temp_extracted_folder)
    subprocess.call(["python", "setup.py", "install"])
    os.chdir("..")
    os.chdir("..")

    shutil.rmtree(temp_folder)

    setup_utilities.log("avro python was installed successfully!")