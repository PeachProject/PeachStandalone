def do():
    import setup_utilities
    setup_utilities.log("Installing pyxnat...")
    setup_utilities.pip_install("pyxnat")
    setup_utilities.log("Successfully installed pyxnat")