from .tag import ZKTag


class ZKTagClient(object):

  def __init__(self, zk_client):
    self._client = zk_client


  def get_by_guid(self, tag_guid):
    en_tag = self._client.get_note_store().getTag(tag_guid)
    return ZKTag(self._client, en_tag)
