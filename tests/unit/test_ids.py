from src.utils.ids import get_uuid_4, get_message_id, get_lease_id


def test_get_uuid_4():
    id1 = get_uuid_4()
    id2 = get_uuid_4()
    assert id1 != id2  # Ensure IDs are unique
    assert len(id1) == 32  # UUID4 hex string length


def test_get_message_id():
    msg_id1 = get_message_id()
    msg_id2 = get_message_id()
    assert msg_id1 != msg_id2  # Ensure message IDs are unique
    assert msg_id1.startswith('msg_')  # Ensure message ID has correct prefix
    assert len(msg_id1) == 36  # 'msg_' + UUID4 hex


def test_get_lease_id():
    lease_id1 = get_lease_id()
    lease_id2 = get_lease_id()
    assert lease_id1 != lease_id2  # Ensure lease IDs are unique
    assert lease_id1.startswith('lease_')  # Ensure lease ID has correct prefix
    assert len(lease_id1) == 38  # 'lease_' + UUID4 hex