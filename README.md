# create-desktop-file.py

## Usage

Say you want to create blender.desktop file in the appropriate place:

    $ ./create-desktop-icon.py blender
    
It will find the executable and default icon path for the application which has to be in the $PATH.

Alternatively you can give the full path to the executable as the second argument:

    $ ./create-desktop-icon.py blender /home/someuser/somepath/blender

## References

Slapped together using:

- https://askubuntu.com/questions/64222/how-can-i-create-launchers-on-my-desktop/64237#64237
- https://askubuntu.com/questions/52430/how-can-i-find-the-location-of-an-icon-of-a-launcher-in-use
- https://gist.github.com/techtonik/4368898
