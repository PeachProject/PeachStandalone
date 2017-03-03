import setup_utilities
from post_venv import setup_flask, install_ldap_python, install_kafka_python, install_avro, install_dask, install_mysql_python, install_pyxnat, install_schedule

setup_flask.do()
install_ldap_python.do()
install_kafka_python.do()
install_avro.do()
install_dask.do()
install_mysql_python.do()
install_schedule.do()
install_pyxnat.do()