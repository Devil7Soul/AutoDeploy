#!/usr/bin/env python3
# Author : YinJun
# Time   : 2020/1/29 9:48
# File   : autodeploy.py
# IDE    : PyCharm

# TODO:This is main execute module. Call core.main module to run the deploy

import sys
sys.path.append('..')

from core import main

settings_list = []
settings = ['IP', 'Port', 'PASSWORD', 'packages']
for index, value in enumerate(settings):
    # print(index, value)
    result = main.analysis_setting(value)
    settings_list.append(result)

ip_list = settings_list[0]
port_list = settings_list[1]
password_list = settings_list[2]
packages_list = settings_list[3]

input_num = str(input('If you want to set the network:'))
if input_num == '1':
    dns1 = 'DNS1=114.114.114.114'
    dns2 = 'DNS2=8.8.8.8'
    a = 'echo %s >> /etc/sysconfig/network-scripts/ifcfg-eth0' %dns1
    b = 'echo %s >> /etc/sysconfig/network-scripts/ifcfg-eth0' %dns2
    c = 'systemctl restart network'
    command = [a, b, c]
    for i in range(len(ip_list)):
        main.run_shell(ip_list[i], password_list[i], port_list[i], *command)
else:
    print('execute the next feature.')

packages_c = []
for i in packages_list:
    packages_c.append('yum -y install '+i)
print(packages_c)

for i in range(len(ip_list)):
    main.run_shell(ip_list[i], password_list[i], port_list[i], *packages_c)

