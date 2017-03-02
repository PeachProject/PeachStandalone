#!/bin/bash
if sudo apt-get install python-apt ; then
    echo "Successfully installed python-apt" ;
    sudo python setup/sudo_setup_pre.py ;
    python setup/non_sudo_setup_pre.py ;
    . venv/bin/activate
    python setup/setup_post.py ;
    python setup/config_editors.py ;
    deactivate ;
fi