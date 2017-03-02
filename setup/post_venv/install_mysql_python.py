def do():
    import setup_utilities
    setup_utilities.log("Installing mysql python module...")
    setup_utilities.pip_install("mysql-connector-repackaged")
    setup_utilities.pip_install("mysql-connector-python")
    setup_utilities.log("Successfully installed mysql python module")