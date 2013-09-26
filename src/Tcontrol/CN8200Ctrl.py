# Author: Bo Wen
# Email: wenboown@gmail.com
# basic control I/O for Omega CN8201 temperature controller

import visa

class CN8201(object):
    '''
    CN8201 vi
    '''

    def __init__(self, com_port):
        '''
        constructor
        '''
        self.vi=visa.SerialInstrument(com_port)
        # for the device we are using, the ID = 01; for CN8200, the zone must be 01
        self.ID_zone="0101"

    def communicate(self, type, param, data):
        string=self.ID_zone+type+param+data
        string="$"+string+self.chesum_calculator(string)
        response=self.vi.ask(string)
        if response[0]!="%":
            return "communication error"
        elif response[5]!=type:
            return "response type error"
        elif response[6:8] != param:
            return "response param error"
        else:
            return response

    def read(self, param):
        string=self.communicate("R",param,"")
        if string[8] != "0":
            return "read response error, code "+string[8]
        elif string[5] == "R":
            return "+" + string[9:15]
        elif string[5] == "r":
            return "-" + string[9:15]
        else:
            return "read response string error"

    def write(self, param, data):
        if data[0] == "-":
            string=self.communicate("w", param, data[1:7])
        else:
            string=self.communicate("W", param, data[1:7])
        return string[8]

    def auxiliary(self, param, data):
        return "function under developing"

    def set_temperature(self, set_point):
        return ""

    def read_temperature(self):
        return ""

    def set_recipe(self):
        return ""

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
