This was created as an experiment in Visual Python, for each animal you input a name, the evolutionary distance from the first animal, and the paralogs with the previous animal in order to create a scale.

Video of program in action: http://www.youtube.com/watch?v=r1C0rxyR9Gg

How to run the file (instructions for someone who has never used python)

First of all, you need to download Python. This is the computer language that the program is written in, and it needs this file in order to interpret and run the program
Windows download: http://www.python.org/ftp/python/3.2.3/python-3.2.3.msi
Mac download: http://www.python.org/ftp/python/3.2.3/python-3.2.3-macosx10.3.dmg

All other download can be found here: http://www.python.org/download/

Then, you need to install the visual libraries to Python, which will allow the graphics in the file to run
Windows download: http://vpython.org/contents/download/VPython-Win-Py3.2-5.74.exe
Mac download: http://vpython.org/contents/download/VPython-Mac-Py3.2-5.74.zip

After that, you need to download the program itself from this github source

Once you have all those files downloaded and installed, just run the python file (the last file you downloaded), and it will give you instructions on how to make the evolutionary tree.

Here is the sample data we have, please feel free to find your own data and send pictures of the evolutionary trees to arya@aryaboudaie.com

How many animals do you want: 5

Name of Organism #1: Horse

Name of Organism #2: Donkey

Evolutionary Distance from Horse: 1

Paralogs with Horse: 8

Name of Organism #3: Chicken

Evolutionary Distance from Horse: 11

Paralogs with Donkey: 10

Name of Organism #4: Penguin

Evolutionary Distance from Horse: 13

Paralogs with Chicken: 15

Name of Organism #5: Snake

Evolutionary Distance from Horse: 21

Paralogs with Penguin: 16



Notice that is asks for evolutionary distance from the first animal, but for paralogs with the previous animal. The scaling for the paralogs (z axis) is 20/z, where z is the number of paralogs in common with the previous animal (so the more paralogs, the closer the animals)


Send any bug reports, screenshots, or suggestions to arya@aryaboudaie.com


(I'll make a video later)
