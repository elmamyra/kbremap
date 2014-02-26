from PySide.QtCore import QObject, QThread, QTimer, Signal

import socket
import data as d
import time

class Network(QObject):
    connected = Signal()
    socketClosed = Signal()
    def __init__(self, parent):
        super(Network, self).__init__(parent)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._isConnected = False
        self.threadRecv = None
        self.timerConnect = QTimer(self)
        self.timerConnect.timeout.connect(self.connect_)
        
#     def serverIsAlive(self):
#         try:
#             self.socket.connect((socket.gethostname(), d.PORT))
#             return True
#         except:
#             return False
    
    def connect_(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((socket.gethostname(), d.PORT))
            self.socket.send('mainwindow')
            self._isConnected = True
            self.timerConnect.stop()
            self.threadRecv = ThreadRecv(self.socket)
            self.threadRecv.closedEvent.connect(self.closed)
            self.threadRecv.start()
            self.connected.emit()
        except:
            self._isConnected = False
            self.timerConnect.start(100)
            
        return self._isConnected
    
    def closed(self):
        self._isConnected = False
        self.socketClosed.emit()
        self.timerConnect.start(100)
    
    def send(self, msg):
        if self._isConnected:
            print 'send'
            self.socket.send(msg)
            
    def stop(self):
        if self.threadRecv:
            self.threadRecv.quit()
            self.threadRecv.wait()
        
    def isConnected(self):
        return self._isConnected
        
#             self.socket.send('quit')
        

class ThreadRecv(QThread):
    closedEvent = Signal()
    def __init__(self, conn):
        QThread.__init__(self)
        self.conn = conn
        self.conn.setblocking(0)
        self.running = True
    
    def quit(self):
        self.running = False
        self.conn.close()
     
    def run(self):
        while self.running:
            try:
                msg = self.conn.recv(128)
            except:
                time.sleep(0.05)
                continue
            if not msg:
                self.closedEvent.emit()
                print 'break'
                break
            
            
