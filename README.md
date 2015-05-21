# ros_workshop

Packages for ROS workshops/seminars held by TORK

# Setups common for all workshops

## Intended Environment

- Ubuntu 14.04 (Trusty Tahr) 64bit
- No virtual machine (it MIGHT work but cannot be guaranteed)
- Intel i5 4th generation or higher
 - You can check by `sudo lshw | grep -i cpu` (ref. [this QA thread](http://askubuntu.com/a/26397/24203))
- 5GB free disk space
- 1 or more USB ports
- When attending a workshop outside your organization, be sure to disable intra-network setting (e.g. web proxy).

## Setup

### System prerequisite 

- Install ROS Indigo by following the installation tutorial [Japanese](http://wiki.ros.org/ja/indigo/Installation/Ubuntu) : [English](http://wiki.ros.org/indigo/Installation/Ubuntu)

### Workshop content
```
sudo apt-get install git
source /opt/ros/indigo/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src && catkin_init_workspace
git clone https://github.com/tork-a/ros_seminar.git
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r  -y
catkin_make
source devel/setup.bash
```
