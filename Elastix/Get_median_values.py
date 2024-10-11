import os
import numpy as np
from my_functions import load_nifti
import matplotlib.pyplot as plt

val = [24482.0,
24415.0,
23895.0,
24479.0,
23161.0,
23863.0,
23578.0,
22794.0,
22552.0,
21863.0,
21186.0,
20593.0,
18409.0]

pressure = [5,10,15,20,25,30,35,40,45,50,55,60,65]

plt.figure()
plt.plot(pressure,val)
plt.xlabel('bar')
plt.ylabel('median value')
plt.title('Attenuation decrease')
plt.show()

# path = r'C:\Users\awias\OneDrive - Danmarks Tekniske Universitet\Documents\Research_Assistant\MicroCracks\Data\pRESSURE\NIFTI'

# files = [x for x in os.listdir(path) if x.endswith('recon.nii') and not x.startswith('.') and not x.endswith('final_recon.nii')]

# for i in range(len(files)):
#     # print(files[i])
#     filename = files[i]
#     img = load_nifti(os.path.join(path,filename))
#     median = np.median(img)
    
#     print(f"{filename}: {median}")
    
    
# '5 bar': 24482.0
# '10 bar': 24415.0
# '15 bar': 23895.0
# '20 bar': 24479.0
# '25 bar': 23161.0
# '30 bar': 23863.0
# '35 bar': 23578.0
# '40 bar': 22794.0
# '45 bar': 22552.0
# '50 bar': 21863.0
# '55 bar': 21186.0
# '60 bar': 20593.0
# '65 bar': 18409.0

