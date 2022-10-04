from psutil import process_iter
from time import sleep

while(1):
    for proc in process_iter():
        if proc.name() == 'software_reporter_tool.exe':
            proc.kill()
    sleep(60)