import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  # 
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import pandas as pd

data = {
    'Nome': ['Leanderson', 'Beatriz', 'Bruno', 'Rebeca', 'Sara', 'Mateus', 'Michele'],
    'Idade': [25, 25, 28, 22, 35, 23, 27],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(data)

moradores_recife = df[df['Cidade'] == 'Recife']

print(moradores_recife)