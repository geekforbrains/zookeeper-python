class ZKUser(object):

  def __init__(self, zk_client):
    self.client = zk_client


  def profile(self):
    return self.client.get_user_store().getUser()


  def public_profile(self, username=None):
    if not username:
      username = self.profile().username
      
    return self.client.get_user_store.getPublicUserInfo(username)
