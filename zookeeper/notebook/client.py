from .notebook import ZKNotebook


class ZKNotebookClient(object):

  def __init__(self, zk_client):
    self.client = zk_client


  def get_single(self):
    """
    Get a single notebook. This is primarily used when connecting via a Single
    Notebook Auth token, as only one notebook will ever be returned.

    """
    notebook = self.client.get_note_store().listNotebooks()[0]
    return ZKNotebook(self.client, notebook)


  def get_by_guid(self, notebook_guid):
    """
    Get an notebook as a ZKNotebook based on the given notebook guid.

    """
    en_notebook = self.client.get_note_store().getNotebook(notebook_guid)
    return ZKNotebook(self.client, en_notebook)
