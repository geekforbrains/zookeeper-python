Zookeeper
=========

A Python tool for taming the Evernote API

The Evernote SDK is clunky and repetitive. I hope Zookeeper will make your work
with their API more enjoyable.


Quick Example
-------------

```python
import zookeeper

# Create Zookeeper client instance
client = zookeeper.create_client(token='<access_token>')


# Get user account details
user = client.user.get_user()
print user.profile()

# Get the default notebook and the note within it
notebook = client.notebooks.get_default()
print notebook

notes = notebook.get_notes()
print notes

# Get the tags for each note
for note in notes:
  print note.get_tags()

# Get the notebook associated with a note
print notes[0].get_notebook()
