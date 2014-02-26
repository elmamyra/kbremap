import argparse
import daemon
import mainWindow
# print sys.argv
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--daemon", action="store_true",
                    help="run the deamon")
parser.add_argument("-q", "--quit", action="store_true",
                    help="close the daemon")


args = parser.parse_args()
if args.quit:
    daemon.close()

elif args.daemon:
    daemon.start()
else:
    mainWindow.start()

