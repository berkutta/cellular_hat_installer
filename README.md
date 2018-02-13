Cellular Module
================

This software is primarly made for my [Cellular Module](https://www.tindie.com/products/kilobyte/raspberry-pi-2g-cellular-hat/). It currently is able to setup a fresh Raspbian Raspberry Pi with all needed Packets and later do the required startup procedure on every Raspberry Pi bootup.


Installation:

Login to your Pi via SSH and execute the following command:
```
sudo apt update && sudo apt install python-serial python-pathlib ppp git && cd /opt && git clone https://github.com/berkutta/cellular_hat_installer.git && cd cellular_hat_installer/ && sudo python start.py install && sudo reboot
```


After the installation your Pi reboots and after that it should automatically connect via Cellular to the Internet! Just connect again via SSH and check the ppp0 interface:
```
# ifconfig ppp0
ppp0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.170.146.237  netmask 255.255.255.255  destination 192.168.254.254
        ppp  txqueuelen 3  (Point-to-Point Protocol)
        RX packets 55  bytes 9627 (9.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 63  bytes 6120 (5.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
