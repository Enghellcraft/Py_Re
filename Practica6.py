import re

txtloc = open("E:\Mate3\Scrips_Python\Python_VSC\Py_Re\localidades.txt").read()
txtprov = open("E:\Mate3\Scrips_Python\Python_VSC\Py_Re\provincias.txt").read()

print(re.findall(r"(?<=\n)[\d]{4}(?=,)|(?<=,)[\d]{2}(?=\n)",txtloc))
print(re.findall(r"[\d]{1,2}",txtprov))
