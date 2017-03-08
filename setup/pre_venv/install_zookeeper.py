def do():
    import setup_utilities
    setup_utilities.log("Installing zookeeper...")
    setup_utilities.apt_install("zookeeperd")
    setup_utilities.log("Successfully installed zookeeper!")