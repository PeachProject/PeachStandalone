python start_up/start_kafka_server.py
. venv/bin/activate

#This will require the screen package to be installed

screen -dmS "backend_consumer_1" bash -c "
. venv/bin/activate;
python PeachBackend/PeachBackend/run_consumers.py --c 1;
deactivate
"

screen -dmS "backend_consumer_2" bash -c "
. venv/bin/activate;
python PeachBackend/PeachBackend/run_consumers.py --c 2;
deactivate
"

screen -dmS "service_list_producer" bash -c 'python PeachBackend/PeachBackend/service_generator/service_list_producer.py -d "PeachDefaultServiceHub" -i ".git" -k "localhost:9092" -sp "PeachBackend/PeachShared/schemas/serviceSchema.avsc" -kt "Service_serviceListUpdated" -s 1'

screen -dmS "flask_web_server" bash -c '
. venv/bin/activate;
export FLASK_APP=app.py;
cd PeachClient;
cd flaskServer;
flask run'

screen -dmS "service_list_consumer" bash -c "
. venv/bin/activate;
python '/home/henry/Desktop/PeachStandalone/PeachClient/PeachShared/library/serviceAgent/serviceListUpdateConsumer.py' --ka 'localhost:9092' --ev 'Service_serviceListUpdated' --temp '/home/henry/Desktop/PeachStandalone/workflow_script_queue/services.avro' --s '/home/henry/Desktop/PeachStandalone/PeachClient/PeachShared/schemas/serviceSchema.avsc'
"

screen -ls

echo "(Ignore if screen was not installed...)"
echo ""
echo "Above you can see all started screen sessions. "
echo "To open the screen session please type in 'screen -r <name>'. Example: 'screen -r flask_web_server'"
echo ""
echo "To stop all processes please call 'pkill screen'."

deactivate