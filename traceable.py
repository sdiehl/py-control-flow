import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Emplict context switch to foo again')

def bar():
    print('Emplict context switch to bar')
    gevent.sleep(0)
    print('Implicit switch switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
