#!/bin/bash

echo Running "dosbox-gui.py"...
python2 dosbox-gui.py
echo Done!

echo Waiting...
read null
echo Done!

echo ---NEXT SESSION BEGIN------------------------------------------------
./debug.sh
