Register Depth
=============
What is it?
-----------

This code can be used to register depth images with respect to parameters given in calib_results.yml.

Build Notes
-----------
**Requirements**

* OpenCV 3.1.0 or later

**Building register depth**

Open a terminal in the directory and enter:

     make registerDepth	   

Usage
-----
**Linux and OS X**

Open a terminal in this directory and enter:

     ./registerDepth [path of depth image]


For registering all the depth images enter:

    for i in ../../LabeledImages/*depth.png
    	do ./registerDepth $i
    done