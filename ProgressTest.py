# http://blog.rtwilson.com/my-top-5-new-python-modules-of-2015/
# https://pypi.python.org/pypi/tqdm
from time import sleep
from tqdm import tqdm

for i in tqdm(range(1000)):
    sleep(0.01)

