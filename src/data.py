from faker import Faker
from time import time
from src.models.student import Department, Student
from typing import List

# [BENCHMARK] benchmarking the data generation process
start_time = time()

students: List[Student] = []
faker = Faker()

for i in range(20):
    students.append(
        Student(
            id=i,
            name=faker.first_name(),
            surname=faker.last_name(),
            age=faker.random_int(min=17, max=45),
            grade=faker.random_int(min=1, max=20),
            absences=faker.random_int(min=0, max=100),
            department=faker.random_element(elements=list(Department))
        )
    )

# [BENCHMARK] Print the time taken to generate the data
end_time = time()
print(f"Data generation completed in {end_time - start_time:.2f} seconds.")
