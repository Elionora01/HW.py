import pandas as pd
import numpy as np
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
categories = np.unique(data['whoAmI'])
one_hot = pd.DataFrame(np.zeros((len(data), len(categories)), dtype=int), columns=categories)
for i, category in enumerate(categories):
one_hot[category] = (data['whoAmI'] == category).astype(int)

one_hot.head()
