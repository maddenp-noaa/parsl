from viz_server.viz_app import app, db
from viz_server.models import *
from viz_server.views import *
import argparse
import daemon

def create_db():
    """ ZZ, what does this fn. do ?
    """
    db.create_all()


def cli_run():

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=5555,
                        help="Viz server will run on this port. Default:5555")
    parser.add_argument("-l", "--logdir", default="viz_server",
                        help="Parsl worker log directory")
    parser.add_argument("--daemonize", action='store_false',
                        help="Start the viz_server as daemon")
    parser.add_argument("--dbpath", default="sqlite:///monitoring.db",
                        help="Enables debug logging")

    parser.add_argument("--debug", action='store_true',
                        help="Enables debug logging")
    print("Starting Parsl Viz Server")
    args = parser.parse_args()

    create_db()

    if args.daemonize:
        print("Starting as a daemon")
        with daemon.DaemonContext():
            app.run(host='0.0.0.0', port=args.port, debug=args.debug)

    else:
        app.run(host='0.0.0.0', port=args.port, debug=args.debug)


#if __name__ == '__main__':
#    cli_run()
