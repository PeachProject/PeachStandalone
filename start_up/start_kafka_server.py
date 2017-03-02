def main():
    result = query_yes_no("Do you want me to start your local kafka server?")
    if result == False:
        print "Kafka server will not be started..."
        print "This could result in errors if not configured properly.\n"
        return
    
    print "Please type in your kafka username:"
    kafka_username = raw_input()
    print "Please type in your kafka user password (maybe twice):"
    import getpass
    pw = getpass.getpass()

    commands = [
        "su -c 'echo {p} | sudo -S nohup ~{u}/kafka/bin/kafka-server-start.sh ~{u}/kafka/config/server.properties > ~{u}/kafka/kafka.log 2>&1 &' {u}".format(p=pw, u=kafka_username)
    ]
    all_commands = "; ".join(commands)
    subprocess_cmd(all_commands)

    print "Successfully started kafka server!\n"


def subprocess_cmd(command):
    import subprocess
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout

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

if __name__ == '__main__':
    main()