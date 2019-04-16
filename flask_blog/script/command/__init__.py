from flask_script import Command, Server,Option
from flask_script.commands import ShowUrls


class SubServer(Server):
    help = description = 'Runs the Flask development server i.e. app.run()'

    def __init__(self, sub_app, host='0.0.0.0', port=5000, use_debugger=None,
                 use_reloader=None, threaded=False, processes=1,
                 passthrough_errors=False, **options):
        super(SubServer, self).__init__(host,
                                        port,
                                        use_debugger,
                                        use_reloader,
                                        threaded,
                                        processes,
                                        passthrough_errors,
                                        **options)
        self.sub_app = sub_app

    def get_options(self):
        options = super(SubServer, self).get_options()

        result = [Option('-s', '--sub',
                         dest='sub',
                         default=self.sub_app)]

        return result + [item for item in options]

    def __call__(self, app, sub, host, port, use_debugger, use_reloader,
                 threaded, processes, passthrough_errors):
        super(SubServer, self).__call__(sub, host, port, use_debugger,
                                        use_reloader, threaded, processes,
                                        passthrough_errors)
