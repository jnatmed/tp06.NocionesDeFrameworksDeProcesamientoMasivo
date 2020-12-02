#!/usr/bin/env python
"""ejecutor.py"""

import subprocess

subprocess.call("python code\punto-1\mapper.py", shell=True)
subprocess.call("python code\punto-1\mapper_sort.py", shell=True)
subprocess.call(r"python code\punto-1\reducer.py", shell=True)
