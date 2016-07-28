Export Layers
=============
What is it?
-----------

Export Layers is a [GIMP](https://www.gimp.org/) plug-in which exports a specified layer as a separate png-image for all images in a directory.

Requirements
------------

* GIMP 2.8 or later
* Python 2.7 or later from the 2.7.x series

Installation
------------

**Windows**

Make sure you installed GIMP with support for Python scripting.

Copy the `export_layers.py` file and the `export_layers` folder to
`[your home folder]\.gimp-2.8\plug-ins` (usually `C:\Users\[your username]\.gimp-2.8\plug-ins`).


**Linux**

Copy the `export_layers.py` file and the `export_layers` folder to
`[your home folder]/.gimp-2.8/plug-ins` (usually `/home/[your username]/.gimp-2.8/plug-ins`).

If necessary, make the `export_layers.py` file executable, e.g. from the terminal:

    chmod +x "export_layers.py"


**OS X**

Copy the `export_layers.py` file and the `export_layers` folder to
`[your home folder]/Library/Application Support/GIMP/2.8/plug-ins` (usually `/Users/[your username]/Library/Application Support/GIMP/2.8/plug-ins`).

If necessary, make the `export_layers.py` file executable, e.g. from the terminal:

    chmod +x "export_layers.py"

GIMP for OS X may have Python 2.6 bundled, which will not work with this plug-in,
since Python 2.7 is required.

To check if the correct version of Python is installed, start GIMP and go to
Filters -> Python-Fu -> Console. The console must display "Python 2.7" or later
from the 2.7.x series. If not, install Python 2.7, open
`/Applications/Gimp.app/Contents/Resources/lib/gimp/2.0/interpreters/pygimp.interp`
and change its contents to the following:

    python=/usr/bin/python
    /usr/bin/python=/usr/bin/python
    :Python:E::py::python:


Usage
-----
** Linux and OS X**

Open a terminal and enter:

     gimp -i -b '(python-export-layers RUN-NONINTERACTIVE "[pattern]" "[directory path]" 0)' -b '(gimp-quit 0)'


For example:

    gimp -i -b '(python-export-layers RUN-NONINTERACTIVE "*.xcf" "/home/[your username]/img_dir" 0)' -b '(gimp-quit 0)'