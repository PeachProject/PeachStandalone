def apt_install(pkg_name):
    import apt
    import sys

    cache = apt.cache.Cache()
    cache.update()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print "{pkg_name} already installed".format(pkg_name=pkg_name)
    else:
        pkg.mark_install()

        try:
            cache.commit()
            print "{pkg_name} installation successful".format(pkg_name=pkg_name)
        except Exception, arg:
            print >> sys.stderr, "Sorry, package installation failed [{err}]".format(err=str(arg))

def pip_install(module_name):
    import pip
    try:
        pip.main(["install", module_name])
        print "{module_name} installation successful".format(module_name=module_name)
    except Exception, arg:
        print >> sys.stderr, "Sorry, pip module installation failed [{err}]".format(err=str(arg))

def log(msg):
    msg = "\n![PeachSETUP]!: {}\n".format(msg)
    print msg

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    import sys
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")