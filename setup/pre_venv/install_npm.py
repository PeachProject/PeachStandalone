def do():
    import setup_utilities
    setup_utilities.log("Installing npm (by installing nodejs)...")
    import subprocess
    subprocess.call(["sudo", "apt-get", "update"])
    setup_utilities.apt_install("curl")
    subprocess.call(["curl", "-sL", "https://deb.nodesource.com/setup_6.x", "|", "sudo", "-E", "bash", "-"])
    subprocess.call(["sudo", "apt-get", "install", "-y", "nodejs"])
    setup_utilities.log("Successfully installed npm!")