import re


def extract_contents(enml):
  """
  Get the content from within the ENML en-note tags.

  """
  return re.search(r'<en-note[^>]*>(.*?)</en-note>', enml, re.S).group(1)


def normalize_enml(enml):
  """
  This is used to bring all forms of ENML up to its "normal" state, before
  running any additional parsing. Most of the mobile device apps don't add new
  lines etc.

  """
  content = extract_contents(entml)

  content = content.replace('\xC2\xA0', ' ')
  content = content.encode('utf-8')
  content = content.replace('</en-media>', '') # Some devices have closing media tags, others dont

  # Convert special chars
  content = content.replace('&amp;', '&')
  content = content.replace('&quot;', '"')
  content = content.replace('&gt;', '>')
  content = content.replace('&lt;', '<')
  content = content.replace('&nbsp;', ' ')

  # Remove anchor tag from inline src/href urls
  content = re.sub(r'(href|src)(=[\'"]?[^<]*)(<a[^>]+>)(.*?)(</a>)', r'\1\2\4', content)

  bits = re.split(r'(<div[^>]*>.*?</div>)', content)

  if bits[0].strip() == '': # Get rid of blank top lines
    bits.pop(0)

  if len(bits) > 0 and '<div>' not in bits[0]:
    bits[0] = '<div>{0}</div>\n'.format(bits[0])

  for k, v in enumerate(bits):
    if not v:
      bits[k] = '\n'

  return ''.join(bits)


def media_to_html(content):
  """
  Converts en-media tags to their appropriate HTML tags.

  """
  media_tags = re.findall(r'<en-media[^>]+>', content, re.DOTALL)

  for media_tag in media_tags:
    new_tag = ''
    media_attr = ''
    media_type = None
    media_hash = None

    # return list of tuples ex: ('type', 'image/jpeg')
    attributes = re.findall(r'([A-Za-z]+)="([^"]+)"', media_tag)

    for a in attributes:
      if a[0] == 'hash':
        media_hash = a[1]

      elif a[0] == 'type':
        media_type = a[1]

      # Build a string of valid attributes to add back to HTML tag
      elif a[0] not in ['hash']:
        media_attr += ' {0}="{1}"'.format(*a)

    if media_type in configs.VALID_MIME_TYPES:
      new_tag = configs.MEDIA_TAGS[configs.VALID_MIME_TYPES[media_type]['type']]
      new_tag = new_tag.replace(':hash:', media_hash)
      new_tag = new_tag.replace(':attr:', media_attr)

    content = content.replace(media_tag, new_tag)

  return content


def enml_to_html(enml):
  """
  Converts ENML to HTML markup.

  """
  pass


def enml_to_markdown(enml):
  """
  Converts ENML to Markdown.

  Note that this does not actually process the Markdown but returns a clean
  string with Markdown compatible text.

  """
  pass
