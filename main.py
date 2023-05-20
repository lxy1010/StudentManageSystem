import pyinputplus
import csv


class StudentManager:
    def __init__(self):
        self.filePath = 'student.csv'
        self.head = 'ID', 'name', ''

    def clear(self):
        with open(self.filePath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.head)

    def read(self):
        with open(self.filePath, 'r') as f:
            reader = csv.reader(f)
        return list(reader)


if __name__ == '__main__':
    StudentManager().clear()
