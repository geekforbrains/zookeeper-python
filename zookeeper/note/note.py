from .notemetadata import ZKNoteMetadata
from .parser import ZKNoteParser


class ZKNote(ZKNoteMetadata):

  def __init__(self, zk_client, en_note):
    super(ZKNote, self).__init__(zk_client, en_note)

    # Additional properties not already set in ZKNoteMetadata
    self.content = en_note.content
    self.content_hash = en_note.contentHash
    self.content_length = en_note.contentLength
    self.resources = en_note.resources


  def to_html(self):
    """
    Get the content of this note and convert it to HTML.

    """
    pass


  def to_markdown(self):
    """
    Get the content of this note and convert it to Markdown.

    """
    pas
