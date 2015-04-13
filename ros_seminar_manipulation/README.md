#ROS Seminar Intermediate - Manipulation

## Intended Environment

- Ubuntu 12.04 64bit
- No virtual machine
- Intel i5 or higher
- 5GB free disk space
- 1 or more USB ports

## Setup


```
sudo apt-get install git
source /opt/ros/hydro/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src && catkin_init_workspace
git clone https://github.com/tork-a/ros_seminar.git
cd ~/catkin_ws
rosdep install --from-paths src --ignore-src -r  -y
catkin_make
source devel/setup.bash
```
