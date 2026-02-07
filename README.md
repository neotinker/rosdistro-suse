# Rosdistro-SUSE - Notes and openSUSE/SLES specific configuration

This git repository is intended to fill the gap between ROS and SUSE. It holds alternate source.list files and some simple "HOWTOs" and notes.

## "ros_external_extras_suse" - This directory contains alternate source.list files
  (This directory gets packaged by OBS separately from the rest of this repostory.)

  Look for the "ros_external_extras_suse" package in the "External Dependencies" project for the ROS version you want to run.

#### Infrastructure and External Dependencies
These files point to the ros-infrastructure.yaml and external_dependencies.yaml files.

These are manditory

- 10-infra.list.master - Production source.list file. To be used in conjuncture with the 20-default.list provided by ROS.
- 10-infra.list.development - Development source.list file. To be used in conjuncture with the 20-default.list provided by ROS.
- 10-suse.list.master - Production file. To be used in conjuncture with the 20-default.list provided by ROS. (Deprecated)
- 10-suse.list.development - development testing. To be used in conjuncture with the 20-default.list provided by ROS. (Deprecated)

#### "Temp" list

This file is used during fast development cycles. You should never need to use this file. It's contents get merged into "20-default.list" and pushed upstream to ros/rosdistro.

- 15-temp.list
- 15-suse-temp.list (Deprecated)

#### These replace the "20-default.list" provided the ROS project

You only need to use these for testing what is being merged upstream before we open a pull request to ros/rosdistro.

- 20-default.list.build_test - development testing config for ROS Melodic on openSUSE/SLES (Deprecated)
- 20-default.list.devel-testing - development testing config for ROS Melodic and Noetic (Deprecated)
- 20-default.list.development - development testing config for ROS Melodic and Noetic (Deprecated)

## Custom Rosdep files - These contain package lookups that we can't upstream.
ros-infrastructure.yaml - Contains package lookups for packages in the ROS Infrastructure repository.

external_dependencies.yaml - Contains package lookups for packages in the External Dependencies repository.

# INDEX

### "ROS Infrastructure" - These are the tools needed to build ROS.

#### ROS1
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:ros-infrastructure

#### ROS2 - In development
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS2:ros-infrastructure:testing

### "External Dependencies" - These are dependencies that are needed to build ROS packages.

#### ROS1 Noetic
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:noetic:external_dependencies

#### ROS1 Melodic
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS1:melodic:external_dependencies

#### ROS2 - In development
 https://build.opensuse.org/project/show/home:neotinker3:ROS:ROS2:external_dependencies:testing
