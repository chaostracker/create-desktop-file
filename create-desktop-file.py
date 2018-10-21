#!/usr/bin/python

import os
import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

template = """#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=@@exec@@
Name=@@name@@
Comment=@@comment@@
Icon=@@icon@@"""

def getAppIconForDefaultTheme(appname):
    """ Finds the highest resolution icon of the app for the default theme"""
    theme = Gtk.IconTheme.get_default()
    found_icon = ""
    for res in range(0, 512, 2):
        icon = theme.lookup_icon(appname, res, 0)
        if icon:
            found_icon = icon.get_filename()
    if found_icon!="":
        return found_icon
    else: 
        return None

def find_executable(executable, path=None):
    """Find if 'executable' can be run. Looks for it in 'path'
    (string that lists directories separated by 'os.pathsep';
    defaults to os.environ['PATH']). Checks for all executable
    extensions. Returns full path or None if no command is found.
    """
    if path is None:
        path = os.environ['PATH']
    paths = path.split(os.pathsep)
    extlist = ['']
    for ext in extlist:
        execname = executable + ext
        if os.path.isfile(execname):
            return execname
        else:
            for p in paths:
                f = os.path.join(p, execname)
                if os.path.isfile(f):
                    return f
    else:
        return None

testapp = sys.argv[1]

executable = find_executable(testapp)
if executable:
    template = template.replace("@@exec@@",executable)
    template = template.replace("@@name@@",testapp)
    template = template.replace("@@comment@@",testapp)
    template = template.replace("@@icon@@",str(getAppIconForDefaultTheme(testapp)))
    filename = os.path.expanduser("~/.local/share/applications/"+testapp+".desktop")
    with open(filename, 'w') as dfile:
        dfile.write(template)
    print("File '" + filename + "' has been created (or overwritten) with contents:")
    print(template)
else:
    print("No app found")