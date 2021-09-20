import pytest
# “Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles,
# And by opposing end them?”

def always_returns_true():
    return True


def test_always_returns_true():
    assert always_returns_true()
