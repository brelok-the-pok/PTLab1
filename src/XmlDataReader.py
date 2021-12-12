from Types import DataType
from DataReader import DataReader

import xml.etree.ElementTree as ET


class XmlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding="utf-8") as file:
            xml_tree = ET.parse(file)
            root = xml_tree.getroot()
            for person in root:
                name = person.tag.replace('_', ' ')
                self.students[name] = []
                for subj in person:
                    self.students[name].append(
                        (subj.tag, int(subj.text or "0"))
                    )
        return self.students
