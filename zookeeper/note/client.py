import evernote.edam.notestore.NoteStore as NoteStore
from evernote.edam.limits.constants import EDAM_USER_NOTES_MAX

from .note import ZKNote


class ZKNoteClient(object):

  def __init__(self, zk_client):
    self.client = zk_client


  def get_by_guid(self, note_guid, **kwargs):
    en_note = self.client.get_note_store().getNote(
      note_guid,
      kwargs.get('with_content', True),
      kwargs.get('with_resources_data', False),
      kwargs.get('with_resources_recognition', False),
      kwargs.get('with_resources_alternateData', False))

    return ZKNote(self.client, en_note)


  def get_by_notebook(self, notebook_guid, **kwargs):
    notes = []

    filter = NoteStore.NoteFilter()
    filter.notebookGuid = notebook_guid

    result = NoteStore.NotesMetadataResultSpec()
    result.includeTitle = kwargs.get('include_title', True)
    result.includeCreated = kwargs.get('include_created', True)
    result.includeUpdated = kwargs.get('include_updated', True)
    result.includeDeleted = kwargs.get('include_deleted', True)
    result.includeUpdateSequenceNum = kwargs.get('include_update_sequence_num', True)
    result.includeTagGuids = kwargs.get('include_tag_guids', True)

    count = 0
    while True:
      offset = count * EDAM_USER_NOTES_MAX
      result = self.client.get_note_store().findNotesMetadata(filter, offset, EDAM_USER_NOTES_MAX, result)

      for en_note_metadata in result.notes:
        notes.append(ZKNote(self, en_note_metadata))

      if (offset + EDAM_USER_NOTES_MAX) >= result.totalNotes:
        break

      count += 1

    return notes
