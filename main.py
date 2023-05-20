import pyinputplus
import csv


class StudentManager:
    def __init__(self):
        self.filePath = 'student.csv'
        self.head = self.read()[0]

    def clear(self):
        with open(self.filePath, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(self.head)

    def reset(self, head):
        self.head = head
        self.clear()

    def read(self) -> list:
        with open(self.filePath, 'r') as f:
            reader = csv.reader(f)
            ls = list(reader)
        return ls

    def add(self, massage: list):
        if len(massage) != len(self.head):
            print('数据异常, 请重试.')
            return
        with open(self.filePath, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(massage)


if __name__ == '__main__':
    StudentManager()
