# http://blog.rtwilson.com/my-top-5-new-python-modules-of-2015/
# https://pypi.python.org/pypi/tqdm
from time import sleep
from tqdm import tqdm, trange

# for i in tqdm(range(1000)):
#     sleep(0.01)


for i in trange(10, desc='1st loop', leave=True):
    for j in trange(5, desc='2nd loop', leave=True, nested=True):
        for k in trange(100, desc='3nd loop', leave=True, nested=True):
            sleep(0.01)





