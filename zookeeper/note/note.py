from .notemetadata import ZKNoteMetadata
#import .parser


class ZKNote(ZKNoteMetadata):

  def __init__(self, zk_client, en_note):
    super(ZKNote, self).__init__(zk_client, en_note)

    # Additional properties not already set in ZKNoteMetadata
    self.content = en_note.content
    self.content_hash = en_note.contentHash
    self.content_length = en_note.contentLength
    self.resources = en_note.resources


  def to_html(self, media_types=[]):
    """
    Get the content of this note and convert it to HTML.

    """
    return parser.enml_to_html(self.content, media_types)


  def to_markdown(self, allowed_html_tags=[], media_types=[]):
    """
    Get the content of this note and convert it to Markdown.

    """
    return parser.enml_to_markdown(self.content)
