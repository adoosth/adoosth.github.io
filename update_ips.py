import os
from ips import ip_dict

for f in os.listdir('./templates'):
    if f.endswith('.txt'):
        with open(f'./templates/{f}', 'r') as file:
            filedata = file.read()
            for key in ip_dict:
                filedata = filedata.replace('{'+ key + '}', ip_dict[key])
            with open(f'./{f}', 'w') as file:
                file.write(filedata)