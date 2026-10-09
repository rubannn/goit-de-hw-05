kafka_config = {
    "bootstrap_servers": ['77.81.230.104:9092'],
    "username": 'admin',
    "password": '***REMOVED***',
    "security_protocol": 'SASL_PLAINTEXT',
    "sasl_mechanism": 'PLAIN'
}

# Ідентифікатор, що додається до імен топіків, щоб вони не дублювалися з іншими студентами
my_name = "mruban"

BUILDING_SENSORS_TOPIC = f"{my_name}_building_sensors"
TEMPERATURE_ALERTS_TOPIC = f"{my_name}_temperature_alerts"
HUMIDITY_ALERTS_TOPIC = f"{my_name}_humidity_alerts"
