# Wayke

the hypest brain sensor u kno


## Muse_desktop_api
utilizes the modified pyrnassus library included in this repo to read alpha, beta and theta sensor data from the Muse and write them to a csv file for later analysis

## pyrnassus-slight_modifications
binding to read sensor data off the Muse, see https://github.com/capitancambio/pyrnassus for more information

## Muse_reactor
Arduino code to create a secondary device to alert users when their focus is waning. Ensure you have the grove rgb_lcd library to run this code properly (thgis code was designed to be used with the grove base shield, with an LED module attached to port D5, a buzzer module attached to D6, a touch sensor attached to D2 and the rgb lcd attached to one of the I2C ports)
