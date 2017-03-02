def do():
    import setup_utilities

    setup_utilities.pip_install("python-ldap")

    setup_utilities.log("Python ldap was installed successfully!")
    