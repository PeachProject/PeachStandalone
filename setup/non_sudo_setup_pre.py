import setup_utilities
from pre_venv import create_venv, init_submodules, configure_mysql_server

init_submodules.do()
create_venv.do()
configure_mysql_server.do()