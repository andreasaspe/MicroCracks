import pickle
import matplotlib.pyplot as plt
import numpy as np
import os

root = r"C:\Users\awias\Documents\MicroCracks\Check_source_intensity"

with open(os.path.join(root,"mean_list"), "rb") as fp:   # Unpickling
    mean_list = pickle.load(fp)

# Beregn varians
variance = np.var(mean_list, ddof=0)  # ddof=0 for populationsvarians, ddof=1 for stikprøvevarians
print(f"Varians: {variance}")

# Beregn standardafvigelse
std_dev = np.sqrt(variance)
print(f"Standardafvigelse: {std_dev}")

# Opret histogram
plt.hist(mean_list, bins=200, edgecolor='black')  # 'bins' bestemmer antallet af søjler
plt.title('Histogram')
plt.xlabel('Værdi')
plt.ylabel('Frekvens')

# Vis histogram
plt.show()