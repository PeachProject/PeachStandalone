def do():
    import setup_utilities
    setup_utilities.log("Installing mysql for python (python-mysqldb)...")
    setup_utilities.apt_install("python-mysqldb")
    setup_utilities.log("Successfully installed mysql for python!")