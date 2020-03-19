# What is it for?

This script is middleware that sits between any arduino that uses Serial communication and sends that data to the vjoy software to emulate a controller, you can adapt it to emulate keyboard and mouse also
This is meant to be an alternative for arduino leonardo
you can find an example for actual usage in my repositories where I use g25 pedals and shifter without the wheel
# Installation

Download repository.
flash arduino/arduino.ino on the arduino
install vjoy http://vjoystick.sourceforge.net/site/index.php/download-a-install

# Usage
the script as distributed needs 2 analog inputs on A0 and A1 and a digital input on D2 on the arduino
flash the arduino script, take note of the com port used by the arduino, don't forget to close any serial window opened
put that com number in main.py at line 13
then run main.py
don't run it blindly, there are comments to guide you

# Contributing
feel free to contribute to this.
Please make sure to update tests as appropriate.

# donations
if you feel that this work was useful, please consider donating here : https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=LEEG7JQ38WG32&source=url

## License
[MIT](https://choosealicense.com/licenses/mit/)
