# Write a Python program to get the Python version you are using

import subprocess

version = subprocess.run("python --version")

print(version)