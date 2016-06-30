# PPMS
Positive Pressure Monitoring System<br />
By Paul Clarke - June 2016

"The cheapest, fastest, and most reliable components are those that aren't there" - Gordon Bell

Synopsis:

This is a Python program for monitoring two pressure sensors as part of a Raspberry Pi Zero closed-loop control system.
The objective being to maintain a higher (positive) internal air pressure as compared to the external air pressure, thus keeping contaminants outside of a gaming PC case.

The system consists of the following physical components;

a) A BMP-280 pressure / temperature sensor mounted internally.<br />
b) A second BMP-280 mounted externally to the case.<br />
c) One or more 12v fans supplying air into the case.<br />
d) Internally mounted and powered, Raspberry Pi Zero.

Sections:

1) Import Adafruit BMP-280 sensor module, read in the data from address 0x76 and 0x77 and assign to variables.<br />
2) Process the data and perform control operations.<br />
3) Write any required data or control variables to a terminal screen and to the Adafruit IO data-logger.
