"""
Example of a dynamic registry using __init_subclass__ and __new__.
A directory crawler/importer is needed to make it truly dynamic
"""

from connector import Connector
from pwr_other import Other


class SharepointConnector(Connector, lookup='sharepoint'):
    """
    Child class of Connector
    """
    def __init__(self, lookup):
        print('New Sharepoint Connector')
        self.is_init = True


class LocalFSConnector(Connector, lookup='localfs'):
    """
    Child class of Connector
    """
    def __init__(self, lookup):
        print('New local Connector')
        self.is_init = True


def main():
    c = Connector('sharepoint')
    l = Connector('localfs')
    s = Connector('sftp')

    _ = ''


if __name__ == '__main__':
    main()
    