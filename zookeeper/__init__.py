from .client import ZKClient


def create_client(**kwargs):
  return ZKClient(**kwargs)
