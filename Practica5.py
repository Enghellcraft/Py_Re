import re

txt = open("E:\Mate3\Scrips_Python\Python_VSC\Py_Re\pedidos.txt").read()

open("pedidos_agrupados.txt", "w")

print(re.findall(r"[\d]{4}\s[A-Z]\d*",txt))