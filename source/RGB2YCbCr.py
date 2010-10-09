#==================================================================================================== 
# File        : RGB2YCbCr.py
# Author      : Ghanshyam
# Dated       : 08.10.2010
# Description : The file converts the Windows style BMP image to YCbCr binary stream 
#               with a OuputFile.YCbCr extention
#               The script shall be run with the argument as the BMP image. The output file 
#               shall be stored in the current directory where the script is executed.
# 
# Rev         : v1.0
# ===================================================================================================
# Change Log  : 
# ===================================================================================================
# Author      Date        Rev     Description
# Shyam   08.10.2010      v1.0    Created initial source code.
#====================================================================================================
# Copyright(c) 2010: 
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
# General Public License as published by the Free Software Foundation version 3 of the License.
#
# This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without 
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details. You should have received a copy of the GNU General Public 
# License along with this program.If not, see <http://www.gnu.org/licenses/>.
# ===================================================================================================


# import the python imaging library : LIBRARIES IMPORT
#!/usr/bin/python
import sys, time
import Image, ImageDraw
import os, math

# Open the RGb file supplied with the script : INPUT FROM COMMAND LINE
if(len(sys.argv) < 1):
    print "Usage : RGB2YCbCr <filename>"
    print "        filename : A valid Windows Bitmap File"
    sys.exit()

# open the bmp image  : OPEN AND CONSUME THE BMP FILE
try:
    BMPImage= Image.open(sys.argv[1])
    print "Opening BMP image ..............................................................[O.K]"
except: 
    print "Error opening \"" + sys.argv[1] + "\". Check if file exists....................[EXIT]"
    sys.exit()

# PARSE FOR SIZE: 
print "Input BMP Image Size'" 
print BMPImage.size
pixel=list(BMPImage.getdata())

Outfile=open('Output.YCbCr', 'w')

Size = BMPImage.size[0]*BMPImage.size[1]
print Size

# Convert to YCbCr
for i in pixel:
    
    ## Y Equation
    Y = math.trunc((0.257 * i[0]) + (0.504 * i[1]) + (0.098 * i[2]) + 16)
    ##Cb Equation
    Cb = math.trunc(((-0.148) * i[0]) - (0.291 * i[1]) + (0.439 * i[2]) + 128)
    ## Cr Equantion
    Cr = math.trunc((0.439 * i[0]) - (0.368 * i[1]) - (0.071 * i[2]) + 128)
    
    print >>Outfile, "%x" % Y 
    print >>Outfile, "%x" % Cb
    print >>Outfile, "%x" % Cr

Outfile.close()

#BMPImage.show()

