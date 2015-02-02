from .user import ZKUser


class ZKUserClient(object):

  def __init__(self, zk_client):
    self.client = zk_client


  def get_user(self):
    return ZKUser(self.client.get_user_store())
