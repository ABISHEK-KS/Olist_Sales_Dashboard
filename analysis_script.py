import pandas as pd
import numpy as np
import os
import pandas_profiling as pp
path = os.getcwd()
files = os.listdir(path)
ind=files.index('analysis_script.py')
files.pop(ind)
print(files)
dashboardindex=files.index('Dashboard.pbix')
files.pop(dashboardindex)
sum=0
count=1
for k in files: 
    filename=k
    file=pd.read_csv(filename)
    
    filedataframe=pd.DataFrame(file)
    filelength=len(filedataframe)
    argname='index'+str(count)+'.html'
    profrep=pp.ProfileReport(filedataframe)
    profrep.to_file(argname)
    count+=1

    sum+=(filelength+1)
    print('File named',filename, 'has',filelength,'columns')
print('Total sum : ',sum)    
