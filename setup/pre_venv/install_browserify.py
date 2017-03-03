def do():
    import setup_utilities
    setup_utilities.log("Installing browserify...")
    import subprocess
    subprocess.call(["sudo", "npm", "install", "-g", "browserify"])
    setup_utilities.log("Successfully installed browserify!")