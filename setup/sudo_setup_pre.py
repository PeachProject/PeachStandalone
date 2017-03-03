import setup_utilities
from pre_venv import install_browserify, install_npm, install_ldap, configure_ldap_server, install_venv, install_mysql_python, install_mysql_server, create_kafka_server, install_phpldapadmin

install_npm.do()
install_browserify.do()
install_ldap.do()
configure_ldap_server.do()
install_phpldapadmin.do()
install_venv.do()
install_mysql_python.do()
install_mysql_server.do()
create_kafka_server.do()