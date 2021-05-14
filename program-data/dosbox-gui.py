import os
import glob
from subprocess import call

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
  def on_installDosboxButton_clicked(self, button):
    os.system("gnome-terminal -- sudo apt-get install dosbox")
    installationDoneLabel.set_text("Command executed!")
  def on_createProfileButton_clicked(self, button):
    os.chdir("../profiles")
    os.system("mkdir " + profilenameInput.get_text())
    os.chdir("./" + profilenameInput.get_text())
    os.system("mkdir C")
    configFile = open("config.conf", "w")
    configFile.write("#This file was created by DOSBox-GUI\n\n[sdl]\nfullscreen=" + str(fullscreenCheckButton.get_active()) + "\nfulldouble=" + str(doubleBufferingCheckButton.get_active()) + "\nfullresolution=desktop\nwindowresolution=original\noutput=surface\nautolock=" + str(lockMouseCheckButton.get_active()) + "\nsensitivity=" + mouseSensitivityInput.get_text() + "\nwaitonerror=true\npriority=higher,normal\nmapperfile=mapper-0.74-3.map\nusescancodes=true\n\n[dosbox]\nlanguage=\nmachine=svga_s3\ncaptures=capture\nmemsize=" + memoryInput.get_text() + "\n\n[render]\nframeskip=" + frameskipInput.get_text() + "\naspect=false\nscaler=normal2x\n\n[cpu]\ncore=auto\ncputype=auto\ncycles=auto\ncycleup=10\ncycledown=20\n\n[mixer]\nnosound=false\nrate=44100\nblocksize=1024\nprebuffer=25\n\n[midi]\nmpu401=intelligent\nmididevice=default\nmidiconfig=\n\n[sblaster]\nsbtype=sb16\nsbbase=220\nirq=7\ndma=1\nhdma=5\nsbmixer=true\noplmode=auto\noplemu=default\noplrate=44100\n\n[gus\ngus=false\ngusrate=44100\ngusbase=240\ngusirq=5\ngusdma=3\nultradir=C:\ULTRASND\n\n[speaker]\npcspeaker=true\npcrate=44100\ntandy=auto\ntandyrate=44100\ndisney=true\n\n[joystick]\njoysticktype=auto\ntimed=true\nautofire=false\nswap34=false\nbuttonwrap=false\n\n[serial]\nserial1=dummy\nserial2=dummy\nserial3=disabled\nserial4=disabled\n\n[dos]\nxms=true\nems=true\numb=true\nkeyboardlayout=" + keyboardLayoutInput.get_text() + "\n\n[ipx]\nipx=false\n\n[autoexec]\nmount C " + '"' + os.getcwd() + "/C" + '"' + "\n")
    if(dDriveCheckButton.get_active() == True):
      configFile.write("mount D " + '"' + dFolderSelector.get_current_folder() + '"' + "\n")
    configFile.write("cls")
    configFile.close()
    os.chdir("../../program-data")
    launchFile = open(os.path.expanduser('~') + "/Desktop/" + profilenameInput.get_text() + ".sh", "w")
    launchFile.write("#!/bin/bash\ndosbox -conf " + '"' + os.getcwd() + "/profiles/" + profilenameInput.get_text() + "/config.conf" +  '"')
    launchFile.close()
    os.system("chmod +x ~/Desktop/" + profilenameInput.get_text() + ".sh")
    creationDoneLabel.set_text("The profile was created! You can run it from the file on your desktop.")


builder = Gtk.Builder()
builder.add_from_file("dosbox-gui.glade")
builder.connect_signals(Handler())

installationDoneLabel = builder.get_object("installationDoneLabel")

fullscreenCheckButton = builder.get_object("fullscreenCheckButton")
doubleBufferingCheckButton = builder.get_object("doubleBufferingCheckButton")
frameskipInput = builder.get_object("frameskipInput")

lockMouseCheckButton = builder.get_object("lockMouseCheckButton")
mouseSensitivityInput = builder.get_object("mouseSensitivityInput")
fullscreenCheckButton = builder.get_object("fullscreenCheckButton")

memoryInput = builder.get_object("memoryInput")

keyboardLayoutInput = builder.get_object("keyboardLayoutInput")

dDriveCheckButton = builder.get_object("dDriveCheckButton")
dFolderSelector = builder.get_object("dFolderSelector")

profilenameInput = builder.get_object("profilenameInput")

creationDoneLabel = builder.get_object("creationDoneLabel")

window1 = builder.get_object("window1")
window1.connect("delete-event", Gtk.main_quit)
window1.show_all()

Gtk.main()
