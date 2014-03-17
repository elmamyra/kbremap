from PySide.QtCore import QObject, QThread, QTimer, Signal

import socket
from kbremap_app import logger, cst
import time


class Network(QObject):
    messageReceived = Signal(str)
    serverClosed = Signal()
    def __init__(self, parent):
        super(Network, self).__init__(parent)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._isConnected = False
        self.log = logger.Logger('client')
        self.threadRecv = None
        self.timerConnect = QTimer(self)
        self.timerConnect.timeout.connect(self.connect_)
        parent.updated.connect(self.slotUpdated)
    
    def state(self):
        return self._state
    
    def connect_(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((socket.gethostname(), cst.PORT))
            self._isConnected = True
            self.timerConnect.stop()
            self.threadRecv = ThreadRecv(self.socket, self.log)
            self.threadRecv.receivedMessage.connect(self.slotMessage)
            self.threadRecv.start()
            self.log.info('client connected')
            self.send('send-state')
        except:
            self._isConnected = False
            self.timerConnect.start(100)

    
    def slotMessage(self, msg):
        self.log.recv(msg)
        if msg == 'socket-closed':
            self._isConnected = False
            self.timerConnect.start(100)
            self.serverClosed.emit()
        else:
            self.messageReceived.emit(msg)
        
        
        
    def send(self, msg):
        if self._isConnected:
            try:
                self.socket.send(msg)
                self.log.send(msg)
            except socket.error, msg:
                self.log.warning('sending failed: %s', msg)

    def stop(self):
        if self.threadRecv:
            self.threadRecv.quit()
            self.threadRecv.wait()
        
    def isConnected(self):
        return self._isConnected
        
    def slotUpdated(self):
        self.send('update')

class ThreadRecv(QThread):
    receivedMessage = Signal(str)
    def __init__(self, conn, log):
        QThread.__init__(self)
        self.log = log
        self.conn = conn
        self.conn.setblocking(0)
        self.running = True
    
    def quit(self):
        self.running = False
     
    def run(self):
        while self.running:
            try:
                msg = self.conn.recv(128)
            except:
                time.sleep(0.05)
                continue
            if not msg:
                self.receivedMessage.emit('socket-closed')
                break
            else:
                self.receivedMessage.emit(msg)
        
        self.log.info('client close')
        self.conn.close()
#             
            
