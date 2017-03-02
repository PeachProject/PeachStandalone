def do():
    import setup_utilities
    import os
    setup_utilities.log("Setting up kafka server...")
    import subprocess
    bat_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "create_kafka_server.bat")
    subprocess.call(". {}".format(bat_file), shell=True)
    setup_utilities.log("Successfully set up kafka server!")
    