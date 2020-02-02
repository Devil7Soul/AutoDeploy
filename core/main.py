#!/usr/bin/env python3
# Author : Kevin
# Time   : 2020/1/29 9:49
# File   : main.py
# IDE    : PyCharm


import paramiko, os

def analysis_setting(item, *args, **kwargs):
    global result
    BASE_DIR = os.path.dirname(os.getcwd())
    f = open(BASE_DIR+'/conf/settings.conf', 'r', encoding='utf-8')
    for i in f:
        if i.startswith('#', 0) or i.startswith('\n', 0, 1):
            continue
        if i.startswith('s', 0):
            continue
        tmp_list = i.split('=')
        if tmp_list[0].strip() == item:
            tmp_str = tmp_list[1].strip()
            result = tmp_str.split(',')
    f.close()
    return result



def run_shell(hostname, passwd, port, *args, **kwargs):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = hostname, port = port, username = 'root', password = passwd)
    # private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    # ssh.connect(hostname = hostname, port = port, username = username, pkey = private_key)
    for i in args:
        print('execute the command:', i)
        stdin,stdout,stderr = ssh.exec_command(i)
        res,err = stdout.read(),stderr.read()
        result = res if res else err
        print(result.decode())
    ssh.close()
    return

# command = ['ls', 'ifconfig']
# run_shell('58.216.47.104', 'dream@2020', 2231, *command)

# def trans_file():   # TODO:continue to optimize
#     private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#     transport = paramiko.Transport(('10.159.24.92', 22222))
#     transport.connect(username='root', pkey=private_key)
#     sftp = paramiko.SFTPClient.from_transport(transport)
#     sftp.put('/root/test.txt', '/root/testnew.txt')
#     transport.close()
#     return
