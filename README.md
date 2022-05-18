Rosdistro-SUSE - Notes and openSUSE/SLES specific configuration

  Because there are some packages that are required by ROS but not available with openSUSE/SLES, we have to maintain some extra repositories needed to build ROS. There are two so far, "ROS Infrastructure" and "External Dependencies".

"ROS Infrastructure" - These are the tools needed to build ROS.

"External Dependencies" - These are dependencies that are needed to build ROS packages.

"ros_external_extras_suse" - This directory contains source.list files
	This directory gets packaged by OBS separately from the rest of this repostory.
