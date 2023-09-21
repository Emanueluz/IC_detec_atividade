 

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
# create a set of 2 test messages that will be published at the same time
msgs = [{'topic': "paho/test/multiple", 'payload': "test 1"}, ("paho/test/multiple", "test 2", 0, False)]

 
# put in your cluster credentials and hostname
auth = {'username': "aaaaa", 'password': "Aa123456"}
client.publish(msgs, hostname="b5b85536bc1e42009bf45c3e2997d02d.s2.eu.hivemq.cloud", port=8883, auth=auth)
