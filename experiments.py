import itertools
import collections

param = 123

values = [('2006-01-05','BUY','RHAT',100,35.14),
          ('2006-01-05','BUY','RHAT',100,35.14)]

p = list(itertools.chain(*values))

print('ok')