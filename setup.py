#!/usr/bin/python
#coding:utf-8
import sys
from cx_Freeze import setup, Executable

path = sys.path
includes = []
excludes = []
packages = ["modules/encryption", "modules/network","modules/permissions"] # Pour importer nos modules dans l'executable final
options = {"path": path,
           "includes": includes,
           "excludes": excludes,
           "packages": packages
           }
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"
setup(
	name = "Projet Aboubacar",
	version = "1.0",
	description = "Encrypt files on windows",
    options = {"build_exe": options},
	executables = [Executable("main.py", base=base)] # Nom du fichier qu'on rend executable
)
