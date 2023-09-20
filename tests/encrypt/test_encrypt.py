from pytest import raises
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with raises(Exception):
        encrypt_message(message=24, key=42)
        encrypt_message(message='ualbax', key='xablau')

    assert encrypt_message(message='xablau', key=10) == 'ualbax'
    assert encrypt_message(message='xablau', key=3) == 'bax_ual'
    assert encrypt_message(message='xablau', key=4) == 'ua_lbax'
