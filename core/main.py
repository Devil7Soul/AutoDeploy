#!/usr/bin/env python3
# Author : Kevin
# Time   : 2020/1/29 9:49
# File   : main.py
# IDE    : PyCharm

import paramiko, os

def analysis_setting():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('dir', BASE_DIR)
    f = open(BASE_DIR+'/conf/settings.conf', 'r', encoding='utf-8')
    ip_list = []
    port_list = []
    password = []
    packages = []
    for i in f:
        if i.startswith('#', 0) or i.startswith('\n', 0, 1):
            continue
        if i.startswith('s', 0):
            continue
        tmp_list = i.split('=')
        if tmp_list[0] == 'IP':
            pass
        tmp_str = tmp_list[1].strip()

        print(tmp_str)
        print(i)
    f.close()
    return

analysis_setting()

def run_shell(hostname, passwd, port = '22222', username = 'root', *args, **kwargs):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname = hostname, port = port, username = username, password = passwd)
    # private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
    # ssh.connect(hostname = hostname, port = port, username = username, pkey = private_key)
    for i in args:
        print(i)
        stdin,stdout,stderr = ssh.exec_command(i)
        res,err = stdout.read(),stderr.read()
        result = res if res else err
        print(result.decode())
    ssh.close()
    return

# def trans_file():   # TODO:continue to optimize
#     private_key = paramiko.RSAKey.from_private_key_file('/root/.ssh/id_rsa')
#     transport = paramiko.Transport(('10.159.24.92', 22222))
#     transport.connect(username='root', pkey=private_key)
#     sftp = paramiko.SFTPClient.from_transport(transport)
#     sftp.put('/root/test.txt', '/root/testnew.txt')
#     transport.close()
#     return
