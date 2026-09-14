class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        while (count < len(students)):
            student = students.pop(0)
            if student == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            else:
                students.append(student)
                count += 1
        return count
        