# Rosdistro-SUSE - Notes and openSUSE/SLES specific configuration

This git repository is intended to fill the gap between ROS and SUSE. It holds alternate source.list files and some simple "HOWTOs" and notes.

## "ros_external_extras_suse" - This directory contains alternate source.list files
  (This directory gets packaged by OBS separately from the rest of this repostory.)
  Look for the "ros_external_extras_suse" package in the "External Dependencies" project for the ROS version you want to run.

- 20-default.list.build_test - original development testing config for ROS Melodic on openSUSE/SLES (Deprecated)
- 20-default.list.devel-testing - Current development testing config for ROS Melodic and Noetic
- 20-default.list.development - Future development testing config for ROS Melodic and Noetic (switching soon)
                                We've broken packages out from rosdep/{base,ruby,python}.yaml that can't be upstreamed
                                to simplify pushing updates upstream.
- 10-suse.list.development - Future development testing. To be used in conjuncture with the 20-default.list provided by ROS.
- 10-suse.list.master - Future production source.list file. To be used in conjuncture with the 20-default.list provided by ROS.

## Custom Rosdep files - These contain package lookups that we can't upstream.
ros-infrastructure.yaml - Contains package lookups for packages in the ROS Infrastructure repository.
external_dependencies.yaml - Contains package lookups for packages in the External Dependencies repository.

# INDEX

"ROS Infrastructure" - These are the tools needed to build ROS.

####ROS1
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:ros-infrastructure

####ROS2 - In development
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS2:ros-infrastructure:testing

"External Dependencies" - These are dependencies that are needed to build ROS packages.

####ROS1 Noetic
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:noetic:external_dependencies

####ROS1 Melodic
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:melodic:external_dependencies

####ROS2 - In development
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS2:external_dependencies:testing
