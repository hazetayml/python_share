'''
Author: Tay Mei Lan (hazetay@gmail.com)
Change: 
- 13 Nov 2020: Adapted from sample code in documentation for package
'''
# instruction
# need to install the qrcode package
# pip install qrcode

import qrcode

img = qrcode.make('https://bit.ly/IPP-MHA')  #Update URL
img.save("test.png")