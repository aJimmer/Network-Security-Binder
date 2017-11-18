# Assignment 2 - Binders

## Team Members
|Member       |Email                          |
|:-----------:|:-----------------------------:|
|Joshua Christ|jchrist@csu.fullerton.edu      |
|Curtis Turner|cjturner714@gmail.com          |
|Tyler McConnell|tylerjamesmcconnell@gmail.com|
|Angel Jimenez|ajimmer92@gmail.com            |


## Overview

### In class we learned about control hijacking attacks and binders of executable files. Implementing these requires understanding of the techniques used for manipulating and combining binary codes. These skills are important for developing vulnerability patches, executing and countering control hijacking attacks, analyzing malware, and in many other facets of network security.

This assignment has two parts. In the first part you will experiment with a primitive technique which can be used for hiding malicious codes on Microsoft Windows systems. In the second part, you are going to implement a program for combining multiple binary executables into a single executable file which when ran executes all the constituent executables. This type of program is called a binder.

## Part I
In order to complete this part you will need a Windows 7 VM which you can find on your
security lab node.
1. Boot your VM.
2. Download the http://www.7-zip.org compression program.
3. Launch the installer and follow the installation instructions.
4. Download the worm.bat file from one of the earlier demos given in class. The file can be found on Titanium. Recall, the file illustrates a very simple Windows worm which can hang your system.
5. Right-click on worm.bat, and from the menu choose 7-zip ! Add to worm.7z
6. Find a .gif image.
7. Copy the .7z and .gif files to the same directory (if you have not already done so).
8. Hold the Shift key and right-click in the directory containing the two files.
9. From the drop-down right-click menu choose: Open command window here.
10. In the terminal window that appears, enter the following command: copy /B <gif file name> + <7z file name> result. For example, copy /B mygifile.gif + myzipfile.7z result.
11. The above command should have created a file called result in the same directory.
12. Rename the result file to result.7z (i.e., append the 7z extension).
13. Try opening the file using the 7-zip program. What happens? (Note: one way to open the file using the 7-zip program is to right-click on result.7z and choose 7-zip ! Open archive. What happens? Are you able to extract and run the worm.bat file inside the archive?

Yes, the worm is successfully executed and eventually hangs the system as processes are continuosly added. (Note that the worm was modified changing the username listed 'Mike' to the user being used in the Windows 7 system 'Administrator')

14. Repeat the above steps, but this time rename the file to result.gif extension.
15. Try opening the file. What happens?

After renaming result to result.gif and double-clicking, we can view the original gif file. The worm isn't executed. However when using 7-zip we can open the result.gif file and from there execute the worm.

1. Explain what is happening. Do some research in order to find out what the above copy command does. In your explanation be sure to explain the role of each argument in the above command. Also, be sure to explain how Windows handles files which leads to the above behavior. Include the answers to these questions in the README file you submit.

Command arguments and their roles
copy: command used to copy file(s) to another location
/B: binary mode, copies file(s) byte for byte
<gif file name>: source, the file to store in the archive
<7z file name>: destination, the archive containing the worm
result: the combined output from the two files, gif and 7z files.

Windows handles files by simply using the file extension to designate the default program used to open the file. For example, a *.html file will likely be opened by Internet Explorer.

Sources:
https://technet.microsoft.com/en-us/library/bb490886.aspx
https://superuser.com/questions/453245/what-exactly-happens-when-you-use-the-copy-b-command

2. How can this technique be used for hiding malicious codes?

This technique is successully able to hide the malicious worm. The result.gif file opens the same way that the original gif file opens. But as mentioned above, the worm.bat file is successfully hidden and can be executed in the 7-zip program.

3. How robust is this technique in terms of avoiding detection by anti-virus tools? You may
need to do some research.

This technique is fairly robust in terms of avoiding detection by anti-virus tools. For example the result.gif was uploaded to VirusTotal and 58/59 of the used anti-virus tools deemed the file "Clean".

We even tested this technique using an EICAR test-file which is often used to test anti-virus tools. The anti-virus tools on VirusTotal scanned this EICAR file and all tools were able to detect the "virus". However using the above technique we copied the EICAR file to the gif file and reuploaded. After scanning 55/59 anti-virus tools deemed the file "Clean" showing that the technique of hiding malware using that technique is fairly effective.

## Part II
## Requirements
* Multix node: `multix.ecs.fullerton.edu`
* VM containing binder:

### Files
* binder.py
* binderbackened.cpp

### Commands
The binder program shall be invoked using:
$python binder.py <PROG1> <PROG2> ... <PROGN>
command line where each PROGi is an executable program. For example,
$python binder.py /usr/bin/ls /usr/bin/pwd
