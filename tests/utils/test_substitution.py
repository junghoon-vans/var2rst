import os
from pathlib import Path

import pytest

from varst.utils.rst_file import RstFile
from varst.utils.substitution import Substitution
from varst.utils.substitution import substitution_text

TEST_DATA_PATH = os.path.join(
    Path(__file__).resolve().parent.parent, 'data',
)


@pytest.fixture
def substitution() -> Substitution:
    rst_file = RstFile(src=os.path.join(TEST_DATA_PATH, 'README.rst'))
    return Substitution(rst_file)


def test_find_substitution(substitution: Substitution):
    none_whitespace = substitution.find("status")
    with_whitespace = substitution.find("with whitespace")

    print(none_whitespace)
    print(with_whitespace)

    with pytest.raises(KeyError):
        substitution.find("not exist name")


def test_create_substitution():
    assert substitution_text("key", "value") == """.. |key| replace:: value"""
