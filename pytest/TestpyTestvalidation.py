import pytest

@pytest.fixture(scope='module')
def prework():
	print("i setup browser instance")
	yield
	print("i teardown browser instance")

def test_initialCheck(preWork):
	print("This is the initial check")
	assert preWork=="fail"

def test_secondCheck(preSetupWork):
	print("This is the second check")