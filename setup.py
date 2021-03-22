import sys
from cx_Freeze import setup, Executable

setup(  name = "test",
        version = "0.1",
        description = "CUI test",
        executables = [Executable("test.py")])