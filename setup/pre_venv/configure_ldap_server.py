def do():
    import setup_utilities
    setup_utilities.log("Configuring ldap server...")

    import subprocess
    subprocess.call(["sudo", "dpkg-reconfigure", "slapd"])