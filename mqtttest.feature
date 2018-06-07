@sdemo @spotdyna-104 @sanity

Feature: Demo behaves
	
Scenario: Prueba de envio de un MQTT backend E2E
  Given un dispositivo final ha finalizado una descarga de una lista de reproducción de contenidos
  When se envia un json MQTT de PUBLICIDAD
  Then Los datos son almacenados en la Base de Datos en la tabla de logs
