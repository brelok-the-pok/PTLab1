from typing import Dict
from Types import DataType


class FindGoodStudents():
    def __init__(self, data: DataType) -> None:
        self.data = data
        
    def find(self) -> list:
        students = list(self.data.keys())
        for key in self.data:
            for subject in self.data[key]:
                if subject[1]  < 76 and key in students:
                    students.remove(key)
        return students
