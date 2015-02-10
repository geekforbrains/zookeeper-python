import os
from nose.tools import *

import zookeeper
from zookeeper.client.client import ZKClient


class TestClient(object):

  def setUp(self):
    self.client = zookeeper.create_client(token=os.environ['ZK_TOKEN'])


  def test_client_instance(self):
    assert_is_instance(self.client, ZKClient)
