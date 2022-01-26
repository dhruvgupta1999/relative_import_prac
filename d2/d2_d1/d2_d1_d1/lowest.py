import sys
sys.path.append('../../../')
from d1.low import low

l = low()
l.fun()

class low2:

    x = 1
    def fun(self):
        print("I'm in p1.low ")