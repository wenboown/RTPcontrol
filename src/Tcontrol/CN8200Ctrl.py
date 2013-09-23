# Author: Bo Wen
# Email: wenboown@gmail.com
# basic control I/O for Omega CN8201 temperature controller

import pyvisa

class CN8201(object):
    '''
    CN8201 vi
    '''

    def __init__(self, com_port):
        '''
        constructor
        '''
        self.vi=pyvisa.SerialInstrument(com_port)

    def read(self, string):
        reading=self.device.ask("$0101"+string)
        return reading

    def write(self, string):
        reading=self.device.ask("$0101"+string)
        return reading

    def set_temperature(self, set_point):

    def read_temperature(self):

    def set_recipe(self):

    def chesum_calculator(self, str):
        '''
        OMEGA checksum
        '''
        t = 0
        for i in str:
            t += ord(i)
        tens = int(t) % 256 / 10
        ones = int(t) % 256 % 10
        if tens > 9:
            return chr(65+tens-10)+chr(48+ones)
        else:
            return chr(48+tens)+chr(48+ones)

__author__ = 'Bohr'
