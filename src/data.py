from faker import Faker
from time import time
from src.models.students_model import Department, Student
from src.utils.unique_id import get_unique_id


# [BENCHMARK] benchmarking the data generation process
start_time = time()

students: list[Student] = []
students_search_indexes: dict[int, str] = {}

faker = Faker()

for i in range(500):
    students.append(
        Student(
            id=get_unique_id(),
            name=faker.first_name(),
            surname=faker.last_name(),
            age=faker.random_int(min=17, max=45),
            grade=faker.random_int(min=1, max=20),
            absences=faker.random_int(min=0, max=100),
            department=faker.random_element(elements=list(Department))
        )
    )
    
    students_search_indexes[i] = (
        f"{students[i].name} {students[i].surname} {students[i].age} "
        f"{students[i].grade} {students[i].absences} {students[i].department}"
    )
    students_search_indexes[i] = students_search_indexes[i].lower()

# [BENCHMARK] Print the time taken to generate the data
end_time = time()
print(f"Data generation completed in {end_time - start_time:.2f} seconds.")
