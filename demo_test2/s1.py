from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


def run(environ,start_response):

    return [b"asdfasdf"]


if __name__ == '__main__':

    run_simple('localhost', 4000, run)

