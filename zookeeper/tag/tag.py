class ZKTag(object):

  def __init__(self, zk_client, en_tag):
    self._client = zk_client
    self._tag = en_tag
    
    self.guid = en_tag.guid
    self.parent_guid = en_tag.parentGuid
    self.name = en_tag.name
    self.update_sequence_num = en_tag.updateSequenceNum
