from evernote.api.client import EvernoteClient

from .. import user, notebook, note, tag


class ZKClient(object):

  def __init__(self, **kwargs):
    self._en_client = EvernoteClient(
      consumer_key=kwargs.get('consumer_key'),
      consumer_secret=kwargs.get('consumer_secret'),
      token=kwargs.get('token'),
      sandbox=kwargs.get('sandbox', False))

    self._user_store = None
    self._note_store = None

    self.user = user.ZKUserClient(self)
    self.notebooks = notebook.ZKNotebookClient(self)
    self.notes = note.ZKNoteClient(self)
    self.tags = tag.ZKTagClient(self)


  def get_user_store(self):
    if not self._user_store:
      self._user_store = self._en_client.get_user_store()
    return self._user_store


  def get_note_store(self):
    if not self._note_store:
      self._note_store = self._en_client.get_note_store()
    return self._note_store
