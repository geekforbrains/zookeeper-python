import evernote.edam.notestore.NoteStore as NoteStore
from evernote.edam.limits.constants import EDAM_USER_NOTES_MAX


class ZKNotebook(object):

  def __init__(self, zk_client, en_notebook):
    self.client = zk_client
    self.notebook = en_notebook
    self.notes = []


  def get_notes(self, **kwargs):
    """
    Get all notes as ZKNote objects contained in this notebook.

    """
    if not self.notes or kwargs.get('force_update', False):
      self.notes = self.client.notes.get_by_notebook(self.notebook.guid, **kwargs)
    return self.notes
