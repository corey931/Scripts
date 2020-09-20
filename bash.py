import subprocess

env = subprocess.call('printenv')
print(str(env))