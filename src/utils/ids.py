import uuid

def get_uuid_4():
  # returns a random UUID (Universally Unique Identifier) as a string.
  return uuid.uuid4().hex


def get_message_id():
    # returns a unique message ID.
    return f'msg_{get_uuid_4()}'


def get_lease_id():
  # returns a unique lease ID.
  return f'lease_{get_uuid_4()}'