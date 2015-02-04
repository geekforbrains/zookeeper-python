class ZKNoteMetadata(object):

  def __init__(self, zk_client, en_note):
    self._client = zk_client
    self._note = en_note
    self._tags = [] # Set during get_tags() method based on en_note.tagGuids

    self.guid = en_note.guid
    self.notebook_guid = en_note.notebookGuid
    self.title = en_note.title
    self.created = en_note.created
    self.updated = en_note.updated
    self.deleted = en_note.deleted
    self.update_sequence_num = en_note.updateSequenceNum
    self.tag_guids = en_note.tagGuids
    self.attributes = en_note.attributes


  def get_full_note(self):
    """
    Get the full note associated with this note metadata.

    """
    return self._client.notes.get_by_guid(self.guid)


  def get_notebook(self):
    """
    Get the notebook associated with this note.

    """
    return self._client.notebooks.get_by_guid(self.notebook_guid)


  def get_tags(self):
    """
    Get all tags as ZKTag objects associated with this note.

    """
    if not self._tags:
      self._tags = [self._client.tags.get_by_guid(t) for t in self.tag_guids]
    return self._tags
