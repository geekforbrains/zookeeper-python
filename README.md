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
user_profile = user.profile()


# Get the default notebook and the notes within it
notebook = client.notebooks.get_default()
notes = notebook.get_notes()


# Get the tags for each note
for note in notes:
  print note.get_tags()

# Or get all tags in a notebook
notebook_tags = notebook.get_tags()


# Get the notebook associated with a note
some_notebook = notes[0].get_notebook()
```
