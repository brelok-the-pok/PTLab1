from typing import Dict, Tuple
from Types import DataType
from FindGoodStudents import FindGoodStudents
import pytest


class TestCalcRating():
    @pytest.fixture()
    def input_data(self) -> Tuple[DataType, list]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 80),
                    ("русский язык", 76),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 61),
                    ("русский язык", 80),
                    ("программирование", 78),
                    ("литература", 97)
                ]
        }
        good_students: list = ["Абрамов Петр Сергеевич"]
        return data, good_students

    def test_init_calc_rating(
            self, input_data: Tuple[DataType, list]
    ) -> None:
        find_good_studensts = FindGoodStudents(input_data[0])
        assert input_data[0] == find_good_studensts.data

    def test_calc(
            self, input_data: Tuple[DataType, list]
    ) -> None:
        good_students = FindGoodStudents(input_data[0]).find()
        for std1, std2 in zip(good_students, input_data[1]):
            assert std1 == std2
