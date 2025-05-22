import pandas as pd
import os 

for filename in os.listdir('.'):
    if filename.endswith('.xlsx'):
        # new_name = int(filename.split('_')[3][5:]) - 1 # dataset number
        # read_file = pd.read_excel(filename)
        # read_file.to_csv(f"{new_name}.csv", index=None, header=True)
        os.remove(filename)
        


