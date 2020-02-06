
import paho.mqtt.client as mqtt
from subprocess import call
import webbrowser
import os
import signal
import subprocess


def callZoom():
    openlink()
    call(["node", "index.js"])


def disConnect():
    print("stop")
    call("exit 1",shell=True)


def openlink():
    url = 'http://localhost:3000/'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


def on_connect(client, userdata, flags, rc):
    print("Connected with Code : " + str(rc))
    print("MQTT Connected.")
    client.subscribe("demo1")


def on_message(client, userdata, msg):
    messageCome = str(msg.payload.decode("utf-8"))
    if(messageCome == "start"):
        callZoom()
    elif(messageCome == "stop"):
        disConnect()
    else:
        print("command not found! ")


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("soldier.cloudmqtt.com", 14222, 60)
    client.username_pw_set("obpkkwdc", "1lUnSF15XpWM")
    # client.connect("smart-teacher.cloudmqtt.com",1883,60)
    # client.username_pw_set("ekrwnxjf","x9OU_vaUyZQJ")
    client.loop_forever()
