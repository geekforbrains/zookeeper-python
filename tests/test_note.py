import os
from nose.tools import *

import zookeeper
from zookeeper.note.note import ZKNote


class TestNote(object):

  def setUp(self):
    self.client = zookeeper.create_client(token=os.environ['ZK_TOKEN'])


  def test_note_to_html(self):
    notebook = self.client.notebooks.get_single()
    note = notebook.get_notes_metadata()[0].get_full_note()
    html = note.to_html()
    assert_true('<div>' in html)
