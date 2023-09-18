import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import random
from faker import Faker

faker = Faker()

nome = faker.name()
idade = random.randint(15, 65)
cidade = faker.city()

print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
