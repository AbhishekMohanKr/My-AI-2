import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyttsx3'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speechrecognition'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'wikipedia'])
