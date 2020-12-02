#!/usr/bin/env python
"""ejecutor.py"""

import subprocess

subprocess.call("python code\punto-2\mapper.py", shell=True)
subprocess.call("python code\punto-2\mapper_sort.py", shell=True)
subprocess.call(r"python code\punto-2\reducer.py", shell=True)
subprocess.call(r"python code\punto-2\reducer_sort.py", shell=True)
