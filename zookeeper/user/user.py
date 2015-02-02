class ZKUser(object):

  def __init__(self, user_store):
    self.user_store = user_store


  def profile(self):
    return self.user_store.getUser()
