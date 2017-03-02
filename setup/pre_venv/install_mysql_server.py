def do():
    import setup_utilities
    setup_utilities.log("Installing mysql server...")
    setup_utilities.apt_install("mysql-server")
    setup_utilities.log("Successfully installed mysql server!")