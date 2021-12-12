import pytest
from typing import Tuple
from Types import DataType
from XmlDataReader import XmlDataReader


class TestXmlDataReader:
    @pytest.fixture()
    def file_and_data_content(self) -> Tuple[str, DataType]:
        text = "<?xml version=\"1.0\" encoding=\"UTF-8\" ?>" +\
               "<root><Иванов_Иван_Иванович>" +\
               "<математика>80</математика>" +\
               "<литература>90</литература>" +\
               "<программирование>76</программирование>" +\
               "</Иванов_Иван_Иванович><Петров_Петр_Петрович>" +\
               "<математика>100</математика>" +\
               "<химия>90</химия>" +\
               "<социология>61</социология>" +\
               "</Петров_Петр_Петрович>" +\
               "</root>"
        data = {
            "Иванов Иван Иванович":
                [
                 ("математика", 80),
                 ("литература", 90),
                 ("программирование", 76)
                ],
            "Петров Петр Петрович":
                [
                 ("математика", 100),
                 ("химия", 90),
                 ("социология", 61)
                ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(
            self, file_and_data_content: Tuple[str, DataType], tmpdir
    ) -> Tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write(file_and_data_content[0])
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: Tuple[str, DataType]) -> None:
        file_content = XmlDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
