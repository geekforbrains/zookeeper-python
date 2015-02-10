import os
from nose.tools import *

import zookeeper
from zookeeper.notebook.notebook import ZKNotebook


class TestNotebook(object):

  def setUp(self):
    self.client = zookeeper.create_client(token=os.environ['ZK_TOKEN'])


  def test_get_single_notebook(self):
    notebook = self.client.notebooks.get_single()
    assert_is_instance(notebook, ZKNotebook)
