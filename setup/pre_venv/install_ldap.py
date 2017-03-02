def do():
    import setup_utilities

    setup_utilities.log("Installing ldap-python prerequisites system-wide...")

    apt_packages = ["libsasl2-dev", "python-dev", "libldap2-dev", "libssl-dev", "slapd", "ldap-utils", "phpldapadmin"]
    for package in apt_packages:
        setup_utilities.apt_install(package)

    setup_utilities.log("Successfully installed ldap-python prerequisites system-wide")

    