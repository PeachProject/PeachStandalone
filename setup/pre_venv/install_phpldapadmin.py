def do():
    import setup_utilities
    answer = setup_utilities.query_yes_no("Do you want to install the php ldap manager (phpldapadmin) and all required web server and PHP dependencies?")
    if answer == False:
        setup_utilities.log("phpldapadmin will not be installed!")
        return
    setup_utilities.log("phpldapadmin will be installed")
    setup_utilities.apt_install("phpldapadmin")
    setup_utilities.log("Sucessfully installed phpldapadmin!")
    