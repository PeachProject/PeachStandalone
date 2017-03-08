def do():
    import setup_utilities
    setup_utilities.log("Installing java (default-jre)...")
    setup_utilities.apt_install("default-jre")
    setup_utilities.log("Successfully installed java!")