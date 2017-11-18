import os
import sys
from subprocess import call
from subprocess import Popen, PIPE

FILE_NAME = "codearray.h";

def getHexDump(execPath):
	
	# The return value
	retVal = None
	
	# TODO:
	# 1. Use popen() in order to run hexdump and grab the hexadecimal bytes of the program.
	# Run the 'hexdump -v -e '"0x" 1/1 "%02X" ","' 
	process = Popen(["hexdump", "-v", "-e", '"0x" 1/1 "%02X" ","', execPath], stdout=PIPE)
	
	# Grab the stdout and the stderr streams
	(output, err) = process.communicate()

	# print(output)

	# Wait for the process to finish and get the exit code
	exit_code = process.wait()

	# 2. If hexdump ran successfully, return the string retrieved. Otherwise, return None.

	if exit_code == 0:
		retVal = output

	# The command for hexdump to return the list of bytes in the program in C++ byte format
	# the command is hexdump -v -e '"0x" 1/1 "%02X" ","' progName
	
	return retVal

def generateHeaderFile(execList, fileName):

	# The header file
	headerFile = None

	# The program array
	progNames = execList

	# Open the header file
	headerFile = open(fileName, "w")

	# The program index
	progCount = len(progNames)

	# The lengths of programs
	progLens = []

	# Write the array name to the header file
	headerFile.write("#include <string>\n\nusing namespace std;\n\nunsigned char* codeArray["+ str(progCount) +"] = {\n\n")

	# Line ending for char arrays
	lineEnd = "} , \n\n"
	
	# TODO: for each program progName we should run getHexDump() and get the 
	# the string of bytes formatted according to C++ conventions. That is, each
	# byte of the program will be a two-digit hexadecimal value prefixed with 0x. 
	# For example, 0xab. Each such byte should be added to the array codeArray in 
	# the C++ header file. After this loop executes, the header file should contain 
	# an array of the following format:
	# 1. unsigned char* codeArray[] = {new char[<number of bytes in prog1>{prog1byte1, prog1byte2.....},
	# 				   new char[<number of bytes in prog2><{prog2byte1, progbyte2,....},
	#					........
	#				};
	
	for prog in range(progCount):
		progBytes = getHexDump(progNames[prog]).split(',')
		byteCount = len(progBytes) - 1

		progLens.append(byteCount)

		headerFile.write("new unsigned char [" + str(byteCount) + "] { ")


		for byte in range(byteCount-1):
			headerFile.write(str(progBytes[byte]) + ", ")

		if prog == progCount-1:
			lineEnd = "}\n\n};"
			
		headerFile.write(str(progBytes[byteCount-1]) + lineEnd)
		

	# Add array to containing program lengths to the header file
	headerFile.write("\n\nunsigned programLengths["+ str(progCount) +"] = {")

	# TODO: add to the array in the header file the sizes of each program.
	# That is the first element is the size of program 1, the second element
	# is the size of program 2, etc.

	for i in range(len(progLens) - 1):
		headerFile.write(str(progLens[i]) + ", ")

	headerFile.write(str(progLens[len(progLens)-1]) + "}; ")
	
	# TODO: Write the number of programs.
	headerFile.write("\n\n#define NUM_BINARIES " +  str(len(progNames)))

	# Close the header file
	headerFile.close()

def compileFile(binderCppFileName, execName):
	
	print("Compiling...")
	
	# Run the process
	# TODO: run the g++ compiler in order to compile backbinder.cpp
	# If the compilation succeeds, print "Compilation succeeded"
	# If compilation failed, then print "Compilation failed"	
	# Do not forget to add -std=gnu++11 flag to your compilation line
	
	if (call(["g++", binderCppFileName, "-o", execName, "-std=gnu++0x"]) == 0):
		print("Compilation succeeded")
	else:
		print("Compilation failed")

generateHeaderFile(sys.argv[1:], FILE_NAME)	
compileFile("binderbackend.cpp", "bound")
