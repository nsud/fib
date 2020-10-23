from flask import Flask
from pymemcache.client.base import Client
import functools
import sys


client = Client(('localhost', 11211))
app = Flask(__name__)


@app.route('/<int:k>', methods=['GET'])
def index(k):
    result = client.get('k')
    mess = 'Число взято из кэша'
    if result is None:
        result = fibo_steroids(k)
        client.set('k', result)
        mess = 'Свежатинка. Число занесено в кэш'

    return f"{mess}\n{k}-ое число Фибоначчи: {str(result)}"


@functools.lru_cache(maxsize=None)
def fibo_steroids(n):
    sys.setrecursionlimit(30000)

    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n - 1) + fibo_steroids(n - 2)


if __name__ == '__main__':
    app.run()