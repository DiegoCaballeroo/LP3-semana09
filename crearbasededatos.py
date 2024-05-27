# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:04:57 2024

@author: Dell
"""

import sqlite3

# Con el comando connect buscará la base de datos
# que tenga ese nombre, de lo contrario lo creará.
conexion = sqlite3.connect("bdbiblioteca.db")
conexion.close()
