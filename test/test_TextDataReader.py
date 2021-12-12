import pytest
from typing import Tuple
from Types import DataType
from TextDataReader import TextDataReader


class TestTextDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> Tuple[str, DataType]:
        text = "Иванов Иван Иванович\n" + \
        " математика:80\n " + \
        " программирование:90\n " + \
        " литература:76\n" + \
        "Петров Петр Петрович\n " + \
        " математика:100\n " + \
        " социология:90\n " + \
        " химия:61"
        data = {
            "Иванов Иван Иванович":
                [
                 ("математика", 80),
                 ("программирование", 90),
                 ("литература", 76)
                ],
            "Петров Петр Петрович":
                [
                 ("математика", 100),
                 ("социология", 90),
                 ("химия", 61)
                ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(
            self, file_and_data_content: Tuple[str, DataType], tmpdir
    ) -> Tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write(file_and_data_content[0])
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: Tuple[str, DataType]) -> None:
        file_content = TextDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
