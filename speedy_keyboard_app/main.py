import argparse
import daemon
import mainWindow
# print sys.argv
parser = argparse.ArgumentParser()

parser.add_argument("-d", "--daemon", action="store_true",
                    help="run the deamon")
parser.add_argument("-p", "--pause", action="store_true",
                    help="pause the daemon")
parser.add_argument("-r", "--resume", action="store_true",
                    help="pause the daemon")
parser.add_argument("-q", "--quit", action="store_true",
                    help="close the daemon")


args = parser.parse_args()
if args.daemon:
    daemon.start()
elif args.quit:
    daemon.close()
elif args.pause:
    daemon.pause()
elif args.resume:
    daemon.resume()

else:
    mainWindow.start()

