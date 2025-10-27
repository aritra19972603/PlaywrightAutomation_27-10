import pytest


@pytest.fixture(scope="session")
def preSetupWork(preWork):
	print("i setup browser instance")