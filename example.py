from tsdb.query import Query
from tsdb.query.filters import *

print(Query('some.metrics').rate(True, 10, 20).aggr('max').filters({
    'a': 'b', 'c': 'd',
    'e': literal_or('f'),
    'g': regexp('.*', groupBy=False),
    'h': not_key(),
}).m())
# max:rate{counter,10,20}:some.metrics{a=b,c=d,e=literal_or(f),h=not_key()}{g=regexp(.*)}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).m())
# sum:some.metrics{a=b,c=d}

##  below are rate examples

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate().m())
# sum:rate:some.metrics{a=b,c=d}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate(counter=True).m())
# sum:rate{counter}:some.metrics{a=b,c=d}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate(counter=True, dropResets=True).m())
# sum:rate{dropcounter}:some.metrics{a=b,c=d}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate(counter=True, counterMax=1, dropResets=True).m())
# sum:rate{dropcounter,1}:some.metrics{a=b,c=d}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate(counter=True, resetValue=1, dropResets=True).m())
# sum:rate{dropcounter,,1}:some.metrics{a=b,c=d}

print(Query('some.metrics').filters({'a': 'b', 'c': 'd'}).rate(counter=False, resetValue=1, dropResets=True).m())
# ValueError: invalid rate params

## todo: Downsampling
