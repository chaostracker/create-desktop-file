#!/usr/bin/env python2.7

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

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

print(getAppIconForDefaultTheme("bl3nder"))