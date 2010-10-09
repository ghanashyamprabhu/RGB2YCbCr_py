Author  : Ghanashyam
Date    : 08.10.2010
Filename: ReadMe

==================================================================================================
ReadMe Information
==================================================================================================

i.  The source code is developed to generate a YCbCr bitstream from a valid Windows BMP image. 
ii. The code is implemented in Python and makes use of the Python Imaging Library.
iii.The imaging library can be installed using the following command 
        sudo apt-get install python-imaging
iv. The code takes an input BMP image and converts the RAW RGB data into a YCbCr bit stream and 
    stores the resulting values in to an output file name same as that of the input file but 
    with a .YCbCr extension(not a standard).
v.  The code uses specific constants for Kb and Kr for extracting the luma and chroma components
    
HOW TO RUN THE CODE:

The code can be run on the linux shell provided there is python installed on the system. Along with
python, python-imaging is also a pre-requisite. The command for running the code is as follows

    $ python RGB2YCbCr.py <BMP_Image_filename> 














==================================================================================================
Copyright(c) 2010: 
This program is free software: you can redistribute it and/or modify it under the terms of the GNU 
General Public License as published by the Free Software Foundation, either version 3 of the 
License.

This program is distributed in the hope that it will be useful,but WITHOUT ANY WARRANTY; without 
even the implied warranty ofMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details. You should have received a copy of the GNU General Public 
License along with this program.If not, see <http://www.gnu.org/licenses/>.
==================================================================================================

