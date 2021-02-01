import sys
import random
import string
import subprocess
all_chs = string.ascii_letters + string.digits
def randpass(n=8):
    rp = ''
    for i in range(n):
        ch = random.choice(all_chs)
        rp += ch
    return rp
def adduser(user, passwd, fname):
    result = subprocess.run('id %s &> /dev/null' % user, shell=True)
    if result.returncode == 0:
        print("用户已存在")
        exit(101)
    subprocess.run('useradd %s' % user,shell=True)
    subprocess.run('echo %s | passwd --stdin %s' % (user, passwd), shell=True)
    with open(fname,'a') as fobj:
        fobj.write('username: %s\npassword: %s\n ' % (username, password))

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass()
    fname = sys.argv[2]
    adduser(username, password, fname)
