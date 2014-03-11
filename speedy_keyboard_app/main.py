import argparse
import daemon


parser = argparse.ArgumentParser()

parser.add_argument("-s", "--start", action="store_true",
                    help="start the server")
parser.add_argument("-p", "--pause", action="store_true",
                    help="pause/resume the server")
parser.add_argument("-q", "--quit", action="store_true",
                    help="close the server")
parser.add_argument("-d", "--debug", action="store_true", 
                    help="show log in console")


args = parser.parse_args()

if args.start:
    daemon.start(args.debug)
elif args.quit:
    daemon.close()
elif args.pause:
    daemon.pause()


else:
    import mainWindow
    mainWindow.start()

