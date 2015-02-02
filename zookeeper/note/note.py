from ..tag import ZKTagClient


class ZKNote(object):

  def __init__(self, zk_client, en_note):
    self.client = zk_client
    self.note = en_note


  def get_notebook(self):
    """
    Get the notebook associated with this note.

    """
    return self.client.notebooks.get_by_guid(self.note.notebookGuid)


  def get_tags(self):
    """
    Get all tags as ZKTag objects associated with this note.

    """
    for tag_guid in self.note.tagGuids:
      return
