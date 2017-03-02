ldap_server = "localhost:389"

def adapt_shared_for_module(module):
    from config_editors import server_config_editor    
    import setup_utilities
    setup_utilities.log("Adapting PeachShared config for module " + module)
    import os 
    dir_path = os.getcwd()
    module_folder = os.path.join(dir_path, module)
    shared_folder = os.path.join(module_folder, "PeachShared")
    shared_config_folder = os.path.join(shared_folder, "library", "config")
    shared_config_in = os.path.join(shared_config_folder, "peachSharedConfig.sample.py")
    shared_config_out = os.path.join(shared_config_folder, "peachSharedConfig.py")
    shared_config = {
        "Parent": module_folder,
        "peach_temp_data": os.path.join(dir_path, "peach_temp_data"),
        "kafka_server": "localhost:9092",
        "ldap_server": ldap_server,
        "peach_service_temp": os.path.join(dir_path, "workflow_script_queue")
    }    

    server_config_editor.adapt_config(shared_config_in, shared_config_out, **shared_config)
    setup_utilities.log("Successfully adapted PeachShared config for module " + module)

def main():
    import setup_utilities
    from config_editors import server_config_editor

    print "Please enter your ldap server / domain you selected at the ldap setup:"
    ldap_server = raw_input()

    import os 
    dir_path = os.getcwd()

    ### Create needed temp folders ###
    ##################################

    setup_utilities.log("Creating needed temp folders...")

    #workflow_script_queue
    workflow_script_queue = os.path.join(dir_path, "workflow_script_queue")
    if not os.path.exists(workflow_script_queue):
        os.makedirs(workflow_script_queue)

    #peach_temp_data
    peach_temp_data = os.path.join(dir_path, "peach_temp_data")
    if not os.path.exists(peach_temp_data):
        os.makedirs(peach_temp_data)
        os.makedirs(os.path.join(peach_temp_data, "workflow_temp"))
        os.makedirs(os.path.join(peach_temp_data, "download_temp"))
        os.makedirs(os.path.join(peach_temp_data, "download_temp", "workflows"))
        os.makedirs(os.path.join(peach_temp_data, "download_temp", "files"))

    setup_utilities.log("Successfully created all needed temp folders")

    ### Adapt configuration files ###
    #################################

    setup_utilities.log("Adapting configuration files")


    #PeachClient
    setup_utilities.log("PeachClient Configuration:")
    PeachClient_Git_Repo = os.path.join(dir_path, "PeachClient")
    flask_sample_config = os.path.join(PeachClient_Git_Repo, "flaskServer", "config", "flaskServerConfig.sample.py")
    flask_output_config = os.path.join(PeachClient_Git_Repo, "flaskServer", "config", "flaskServerConfig.py")
    flask_server_config = {
        "PeachClient_Git_Repo": PeachClient_Git_Repo,
        "peach_temp_data": peach_temp_data,
        "mysql_host": "localhost:3306",
        "mysql_user": "peach",
        "mysql_pw": "peachuser",
        "mysql_database": "peach",
        "current_domain": "http://localhost:5000"
    }

    server_config_editor.adapt_config(flask_sample_config, flask_output_config, **flask_server_config)

    adapt_shared_for_module("PeachClient")

    setup_utilities.log("Successfully configured PeachClient!")

    #PeachBackend
    setup_utilities.log("PeachBackend Configuration:")

    backend_current_git = os.path.join(dir_path, "PeachBackend")
    backend_sample_config = os.path.join(backend_current_git, "PeachBackend", "config", "peachBackendConfig.sample.py")
    backend_output_config = os.path.join(backend_current_git, "PeachBackend", "config", "peachBackendConfig.py")

    backend_config = {
        "current_git": backend_current_git,
        "local_queue_temp": workflow_script_queue,
        "Peach_Service_Hub": os.path.join(dir_path, "PeachDefaultServiceHub"),
        "Kafka_Server": "localhost:9092",
        "mysql_host": "localhost:3306",
        "mysql_user": "peach",
        "mysql_pw": "peachuser",
        "mysql_database": "peach"
    }

    server_config_editor.adapt_config(backend_sample_config, backend_output_config, **backend_config)

    adapt_shared_for_module("PeachBackend")

if __name__ == '__main__':
    main()