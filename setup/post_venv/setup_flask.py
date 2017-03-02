def do():
    import setup_utilities
    setup_utilities.log("Installing Flask...")
    
    setup_utilities.pip_install("Flask")

    setup_utilities.log("Flask-Installation successful!")