# 2. Write a python script which will display system name ,node name and release details of current system.

import os
import socket
import platform

os.uname().nodename

'''platform.node()
platform.system()
platform.release()
platform.version()

socket.gethostname()'''