python start_up/start_kafka_server.py
. venv/bin/activate

cd PeachBackend
cd PeachBackend
python run_consumers.py
cd ..
cd ..


gnome-terminal -x sh -c 'python PeachBackend/PeachBackend/service_generator/service_list_producer.py -d "PeachDefaultServiceHub" -i ".git" -k "localhost:9092" -sp "PeachBackend/PeachShared/schemas/serviceSchema.avsc" -kt "Service_serviceListUpdated" -s 1'

gnome-terminal -x sh -c 'export FLASK_APP=app.py;
cd PeachClient;
cd flaskServer;
flask run'


deactivate