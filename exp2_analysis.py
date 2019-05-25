import numpy as np

exps = [
    {'exp': {
        'tag': "2a",
        'lables': "# m delta_m x delta_x\n",
        'errs': [2, 0.1] 
    }}, {'exp': {
        'tag': "2b",
        'lables': "# m delta_m x delta_x\n",
        'errs': [2, 0.1]
    }}
]

finbase = 'data/exp'
foutbase = 'analysis/exp'

for exp in exps:
    print(exp['exp']['lables'])

    fin = finbase + exp['exp']['tag'] + '.csv' 
    fout = foutbase + exp['exp']['tag'] + '.dat'
    outfile = open(fout, "w+")
    
    outfile.write(exp['exp']['lables'])

    with open(fin) as f:
        content = f.readlines()

    for row in content:
        row_data = row.split(",")

        col1 = float(row_data[0])
        delta_col1 = float(exp['exp']['errs'][0])

        col2 = float(row_data[1])
        delta_col2 = float(exp['exp']['errs'][1])

        str1 = str(col1) + " " + str(delta_col1) + " "
        str2 = str(col2) + " " + str(delta_col2) + "\n"

        outfile.write(str1 + str2)

    outfile.close()


