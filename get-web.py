import os
import wget
import re
def get_patt(fname, patt, charset=None):
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=charset) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                result.append(m.group())
    return result

if __name__ == '__main__':
    dst = '/tmp/163'
    fname163 = '/tmp/163/163.html'
    url = 'http://www.163.com'
    if not os.path.exists(dst):
        os.mkdir(dst)
    if not os.path.exists(fname163):
        wget.download(url, fname163)
    img_patt = '(http|https)://[\w/.-]+\.(jpg|jpeg|png|gif)'
    img_list = get_patt(fname163, img_patt, 'gbk')
    for img_url in img_list:
        wget.download(img_url, dst)

