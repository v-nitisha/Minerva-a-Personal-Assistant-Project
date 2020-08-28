# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 16:15:38 2020

@author: Vera J. Morgana
"""

import pymysql

pymysql.install_as_MySQLdb()

db= MySQLdb.connect("hostname", "username", "password", "database_name")