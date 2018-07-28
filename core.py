#!/usr/bin/env python3
import os
import sys
import subprocess
from enum import Enum

Type = Enum('Type', 'A a B b D d f L l T t U')

fileName = "ex"
functions = []

class Function:
    address = ""
    size = 0
    function_t = Type.U
    name = ""

    def __init__(self, address, size, function_t, name):
        self.address = address
        self.size = size
        self.function_t = function_t
        self.name = name


stdout = subprocess.check_output(["nm", "-C", "--print-size", "--size-sort", fileName]).decode("utf-8")


for line in stdout.split("\n"):
    elem = line.split(" ")
    if len(elem) == 4:
        functions.append(Function(elem[0], elem[1], elem[2], elem[3]))

