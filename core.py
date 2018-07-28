import os
import sys
from subprocess import call


class Function:
    address = 0
    size = 0
    type = ""
    name = ""

    def __init__(self, address, size, type, name):
        self.address = address
        self.size = size
        self.type = type
        self.name = name

