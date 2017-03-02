def do():
    import setup_utilities
    setup_utilities.log("Installing python schedule...")
    setup_utilities.pip_install("schedule")
    setup_utilities.log("Successfully installed python schedule!")