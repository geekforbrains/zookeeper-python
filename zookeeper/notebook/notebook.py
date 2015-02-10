import evernote.edam.notestore.NoteStore as NoteStore
from evernote.edam.limits.constants import EDAM_USER_NOTES_MAX


class ZKNotebook(object):

  def __init__(self, zk_client, en_notebook):
    self._client = zk_client
    self._notebook = en_notebook
    self._notes_metadata = []

    self.guid = en_notebook.guid
    self.name = en_notebook.name
    self.update_sequence_num = en_notebook.updateSequenceNum


  def get_notes_metadata(self, **kwargs):
    """
    Get all notes as ZKNoteMetadata objects contained in this notebook.

    """
    if not self._notes_metadata or kwargs.get('force_update', False):
      self._notes_metadata = self._client.notes.get_by_notebook(self.guid, **kwargs)
    return self._notes_metadata
