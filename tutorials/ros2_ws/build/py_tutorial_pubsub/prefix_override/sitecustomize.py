import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/sam-robot-pi/Documents/ros-dev/tutorials/ros2_ws/install/py_tutorial_pubsub'
