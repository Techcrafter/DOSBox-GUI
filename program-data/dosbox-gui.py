import os
import glob
from subprocess import call

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
  def on_installDosboxButton_clicked(self, button):
    os.system("gnome-terminal -- sudo apt-get install dosbox")
    installationDoneLabel.set_text("Done!");

builder = Gtk.Builder()
builder.add_from_file("dosbox-gui.glade")
builder.connect_signals(Handler())

installationDoneLabel = builder.get_object("installationDoneLabel")

window1 = builder.get_object("window1")
window1.connect("delete-event", Gtk.main_quit)
window1.show_all()

Gtk.main()
