from .tag import ZKTag


class ZKTagClient(object):

  def __init__(self, zk_client):
    self.client = zk_client
