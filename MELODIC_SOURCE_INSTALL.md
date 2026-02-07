# MELODIC SOURCE INSTALLATION

### I'm keeping and cleaning up this document for historical purposes but you probably shouldnt use it

## PREAMBLE
Currently, we *CAN* build all the metapackage variants for Opensuse 15.1, 15.2, and 15.3 (x86_64). We can also build all the metapackages for SLES 15 SP3. We are missing some graphics libraries on other architectures, at the moment.

https://github.com/ros/metapackages.

I have created two projects in the OpenSUSE Build Service, "ROS:External_Dependencies" and "ROS:ros-infrastructure". The "ROS:ros-infrastructure" project contains builds of the ROS tools needed to start building ROS applications. The "ROS:External_Dependencies" project is where I am maintaining builds of any ROS dependencies which don't exist in either openSUSE or SLES.

https://build.opensuse.org/project/show/home:neotinker3:ROS:ros-infrastructure

https://build.opensuse.org/project/show/home:neotinker3:ROS:External_Dependencies

Currently, I am maintaining my own rosdistro with custom modifications for Opensuse Leap and SLES at https://github.com/neotinker/rosdistro. You must use the "build_test" branch to get functional dependencies. I'm in the process of pushing these upstream to ros/rosdistro.

## GOAL
The goal is to be able to follow the Installing from Source Wiki ( http://wiki.ros.org/melodic/Installation/Source ) but there are currently a few differences. I've broken out the steps that are different below.

### For section 1.1, "Installing bootstrap dependencies"

1) Install the "ros-infrastructure" and "External Dependiencies" repos for your OS. You may need extra extensions/modules installed for SLES. The example below is for openSUSE 15.1. Replace "openSUSE_Leap_15.1" with the appropriate OS name and version.

$ sudo zypper --gpg-auto-import-keys ar -f -n "ROS Infrastructure (openSUSE_Leap_15.1)" http://download.opensuse.org/repositories/home:/neotinker3:/ROS:/ros-infrastructure/openSUSE_Leap_15.1/ ROS-Infrastructure
$ sudo zypper --gpg-auto-import-keys ar -f -n "ROS External Dependencies (openSUSE_Leap_15.1)" https://download.opensuse.org/repositories/home:/neotinker3:/ROS:/External_Dependencies/openSUSE_Leap_15.1/ ROS-External-Dependencies
$ sudo zypper refresh

2) Install "base" packages

$ sudo zypper in gcc-c++ python2-rosdep python2-rosinstall_generator python2-wstool python2-rosinstall libboost_system1_66_0-devel libboost_chrono1_66_0-devel libboost_date_time1_66_0-devel libboost_serialization1_66_0-devel libboost_thread1_66_0-devel libboost_filesystem1_66_0-devel libboost_program_options1_66_0-devel liblz4-devel libboost_signals1_66_0-devel libboost_regex1_66_0-devel python3-vcstool ros_external_cmake_modules

If you have X11 installed, you should already have these but if you encounter an error in compiling apps (ex. pcl_ros or gazebo_ros), then make sure these rpms are installed.

$ sudo zypper in glew-devel sqlite3-devel proj-devel libxml2-devel python3-devel libXt-devel jsoncpp-devel libjpeg8-devel

To use my forked rosdistro, install the ros_external_extras_suse rpm. It contains a modified "20-default.list" file that will need to be copied to /etc/ros/rosdep/sources.list.d/

$ sudo zypper in ros_external_extras_suse

You will most likely encounter a conflict between Poco and vtk due to the use of unixODBC and iodbc. I've included a version of Poco in the "External Dependency" repo that is build against iodbc. You may need to force the install of libiodbc-devel (from the OS) and poco-devel (from "External Dependencies). This will most likely pull in a few hundred packages.

### For section 1.2, "Initializing rosdep"

1) Initialize rosdep sources

$ export ROSDISTRO_INDEX_URL=https://raw.githubusercontent.com/neotinker/rosdistro/build_test/index-v4.yaml
$ sudo rosdep init

2) Update the rosdep sources to point to my git repo

If you installed the ros_external_extras_suse rpm, then copy the provided "20-default.list.build_test" to /etc/ros/rosdep/sources.list.d/20-default.list

$ sudo cp /usr/share/ros/20-default.list.build_test /etc/ros/rosdep/sources.list.d/20-default.list

3) Update sources

$ rosdep update

### Follow sections 2 through 2.1.1 as specified in the source install wiki.
Before you run the "vcs import src" command, you need to make sure the "src" directory exists. If any thing else doesn't work, let me know.

### For section 2.1.2, "Building the catkin Workspace"

1) Force catkin_make_isolated to use python 2.7

I suppose it should be possible to force python 3.6 but I haven't tested it yet. If you don't force the use of one python interpreter, the packages with use a mix of both and some will fail due to missing dependencies that aren't getting built.

$ ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python

I'll try to keep this description updated with what is working. And this description should shrink as I resolve pending issues.

## See also
https://github.com/ros-infrastructure

https://github.com/ros/rosdistro
