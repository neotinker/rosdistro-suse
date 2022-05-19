# Rosdistro-SUSE - Notes and openSUSE/SLES specific configuration

This git repository is intended to fill the gap between ROS and SUSE. It holds alternate source.list files and some simple "HOWTOs" and notes.

## "ros_external_extras_suse" - This directory contains alternate source.list files
  (This directory gets packaged by OBS separately from the rest of this repostory.)
  https://build.opensuse.org/package/show/home:neotinker3:ROS:External_Dependencies/ros_external_extras_suse

- 20-default.list.build_test - original development testing config for ROS Melodic on openSUSE/SLES (Deprecated)
- 20-default.list.devel-testing - Current development testing config for ROS Melodic and Noetic
- 20-default.list.development - Future development testing config for ROS Melodic and Noetic (switching soon)
                                We've broken packages out from rosdep/{base,ruby,python}.yaml that can't be upstreamed
                                to simplify pushing updates upstream.
- 10-suse.list.development - Future development testing. To be used in conjuncture with the 20-default.list provided by ROS.
- 10-suse.list.master - Future production source.list file. To be used in conjuncture with the 20-default.list provided by ROS.

ros-infrastructure.yaml - Contains package lookups for packages in the ROS Infrastructure repository.
external_dependencies.yaml - Contains package lookups for packages in the External Dependencies repository.

# INDEX

"ROS Infrastructure" - These are the tools needed to build ROS.
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ros-infrastructure

"External Dependencies" - These are dependencies that are needed to build ROS packages.
 https://build.opensuse.org/project/show/home:neotinker3:ROS:External_Dependencies

