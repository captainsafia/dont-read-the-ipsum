from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from werkzeug.serving import run_simple
from apps.api import api
from apps.front import app as front

application = DispatcherMiddleware(front, {
    "/api": api
})

if __name__ == "__main__":
    run_simple("localhost", 5000, application, use_reloader = True, 
            use_debugger=True)
