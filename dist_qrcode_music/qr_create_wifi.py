'''
Author: Tay Mei Lan (hazetay@gmail.com)
Change: 
- 13 Mar 23: Adapted from sample code in documentation for package
'''
# instruction
# need to install the wifi_qrcode_generator package
# pip install wifi_qrcode_generator

import wifi_qrcode_generator.generator

#ToDo: update SSID and password of the network
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid='SSID', hidden=False, authentication_type='WPA', password='password')
qr_code.print_ascii()
qr_code.make_image().save('wifiqr.png')