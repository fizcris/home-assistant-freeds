[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/fizcris)


# Freeds for Home Assistant

This integration aims to create the sensors/switches in home assist in order to retrieve data and control the freeds from home asistant via MQTT.


* Values will be preseted as sensors.
* Commands will be presented as switches.

# Requeriments

* A freeds device
* A configured MQTT broker (e.g. Mosquitto Broker)

# HACS installation

TODO

# Manual Installation

Create a directory called freeds in the <config directory>/custom_components/ directory on your Home Assistant instance. Install this component by copying all files in /custom_components/freeds/ folder from this repo into the new <config directory>/custom_components/goodwe/ directory you just created.

This is how your custom_components directory should look like:



```bash
custom_components
├── freeds
│   ├── __init__.py
│   ├── freeds.py
│   ├── manifest.json
│   └── sensor.py
```

## Configuration example

To enable this sensor, add the following lines to your `configuration.yaml` file:

```YAML
sensor:
  - platform: freeds
    ip_address: 192.168.100.100
    port: 8899
    baseTopic: freeds_d4ae
    username: MQTT_user
    password: MQTT_password    
```

Be aware that the comunication with your inverter/meter should be preconfigured in freeds previously.



**This component will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from blueprint API.
`switch` | Switch something `True` or `False`.


[Riemann Sum](https://www.home-assistant.io/integrations/integration/) integration can be used to convert these instant (W) values into cumulative values (Wh).  
[Utility Meter](https://www.home-assistant.io/integrations/utility_meter) can report these values as human readable statistical values.  
[Template Sensor](https://www.home-assistant.io/integrations/template/) can be used to separate buy and sell values.

## Inverter communication testing

To test whether the inverter properly responds to UDP request, just execute the `inverter_test.py` script