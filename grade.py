from dataclasses import dataclass

@dataclass
class Grade:
    grade:int
    letter_grade:str = ""

    @staticmethod
    def get_letter(grade):
            if grade >= 88:
                return "A"
            elif grade >= 80:
                return "B"
            elif grade >= 68:
                return "C"
            elif grade >= 60:
                return "D"
            else:
                return "F"