def do():
    import setup_utilities
    import shutil
    setup_utilities.log("Configuring mysql server...")
    import os
    temp_folder = ".temp"
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    full_sql_file = os.path.join(temp_folder, "full_sql.sql")

    prepend_sql_file = "setup/sql/prepend.sql"
    append_sql_file = "PeachBackend/PeachBackend/sql/workflow_execution_queue.sql"

    filenames = [prepend_sql_file, append_sql_file]
    with open(full_sql_file, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                outfile.write(infile.read())

    #mysql -u username -p database_name < file.sql

    print "Thank you..."

    setup_utilities.log("Importing mysql setup file...")

    print "Please put in the mysql root password you just set..."
    import subprocess
    cmd = "mysql -u root -p < {}".format(full_sql_file)
    subprocess.call(cmd, shell=True)

    setup_utilities.log("Successfully imported mysql setup file!")

    setup_utilities.log("Successfully configured mysql server!")

    shutil.rmtree(temp_folder)