import pytest


@pytest.fixture
def v1_trap_example():
    yield b'0:\x02\x01\x00\x04\x06public\xa4-\x06\x05*\x03\x04\x05\x06@\x04\x01\x02\x03\x04\x02\x01\x06\x02\x01cC\x0170\x150\x13\x06\x053\x0c\r\x0e\x0f\x04\nteststring'