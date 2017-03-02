def do():
    import setup_utilities

    setup_utilities.log("Installing virtualenv in /venv ...")

    import platform
    main_version = int(platform.linux_distribution()[1].split(".")[1])
    virtual_env_package = "python-virtualenv" if (main_version <  16) else "virtualenv"
    
    setup_utilities.apt_install(virtual_env_package)

if __name__ == '__main__':
    install_venv()