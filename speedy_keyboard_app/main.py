import argparse
import daemon


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--start", action="store_true",
                    help="start the server")
parser.add_argument("-p", "--pause", action="store_true",
                    help="pause/resume the server")
parser.add_argument("-q", "--quit", action="store_true",
                    help="close the server")


args = parser.parse_args()
if args.start:
    daemon.start()
elif args.quit:
    daemon.close()
elif args.pause:
    daemon.pause()

else:
    import mainWindow
    mainWindow.start()

