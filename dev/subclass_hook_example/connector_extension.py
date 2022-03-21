
from connector import Connector

class SFTPConnector(Connector, lookup='sftp'):
    """
    Child class of Connector
    """
    def __init__(self, lookup):
        print('New sftp Connector')
        self.is_init = True