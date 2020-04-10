To setup an InkyWhat:

# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-what
curl https://get.pimoroni.com/inky | bash
cd /home/pi/Pimoroni/inky/examples/what
python quotes-what.py --colour "black"

# If I2C fails...
sudo raspi-config
Advanced options > Enable I2C
Reboot


