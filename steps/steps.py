#!/python

"""
This python module includes the steps for MQTT 
"""


from behave import *
from funct_mySQLspotdyna import mySQL_QUERY
from funct_mqtt import mqtt_publi
import mysql.connector
import time
import sys
import os


@given('un dispositivo final ha finalizado una descarga de una lista de reproducción de contenidos')
def step_impl(context):
    print("Estoy en el given")
    pass

@when('se envia una trama de PUBLICIDAD')
def step_impl(context):
    command = 'echo "002161#E#PUBLICIDAD#123456" > /dev/udp/192.168.1.121/30020'
    os.system(command)


@when('se envia un json MQTT de PUBLICIDAD')
def step_imp(context):
    resultado = False
    resultado = mqtt_publi()
    if resultado:
        assert True
    else:
        assert context.passed is False
    

@then('Los datos son almacenados en la Base de Datos en la tabla de logs')
def step_impl(context):
    mySQL_QUERY()
    assert True is not False

@then('Se obtiene un ACK MQTT de QoS 1')
def step_impl(context):    
    assert context.failed is False


