import pandas as pd
import numpy as np

data1=pd.read_csv('scimagojr 2017  Subject Area - Computer Science(1).csv',sep=';',usecols=['Title','SJR','H index','Total Docs. (2017)','Total Docs. (3years)','Total Refs.','Total Cites (3years)','Citable Docs. (3years)','Cites / Doc. (2years)','Ref. / Doc.'])
data2=pd.read_csv('found.txt',sep=';',header=None,names=['Title','H index','Impact Factor'])

def merge(df):
	global data2
	for i in range(len(data2['Title'])):
		if df['Title']==data2['Title'][i]:
			return data2['Impact Factor'][i]
		
	return -1

data1['Impact Factor']=data1.apply(merge,axis=1)

l=[]
for i in range(len(data1['Impact Factor'])):
	if (data1['Impact Factor'][i]+1)<10**-6:
		l.append(i)
	#print(data1['Impact Factor'][i])
l.append(1441)
for i in l:
	data1.drop(i,inplace=True)

li=list(data1['SJR'].to_dict().keys())
#print(li)

for i in li:
	for j in range(len(data1['SJR'][i])):
		if data1['SJR'][i][j]==',':
			data1['SJR'][i]=int(data1['SJR'][i][:j]+data1['SJR'][i][j+1:])
			#print(data1['SJR'][i],type(data1['SJR'][i]))
			break
			
		#data1['SJR'][i]=int(data1['SJR'][i])

	for j in range(len(data1['Cites / Doc. (2years)'][i])):
		if data1['Cites / Doc. (2years)'][i][j]==',':
			data1['Cites / Doc. (2years)'][i]=data1['Cites / Doc. (2years)'][i][:j]+'.'+data1['Cites / Doc. (2years)'][i][j+1:]
			data1['Cites / Doc. (2years)'][i]=float(data1['Cites / Doc. (2years)'][i])
			#print(data1['SJR'][i],type(data1['SJR'][i]))
			break
	
	for j in range(len(data1['Ref. / Doc.'][i])):
		if data1['Ref. / Doc.'][i][j]==',':
			data1['Ref. / Doc.'][i]=data1['Ref. / Doc.'][i][:j]+'.'+data1['Ref. / Doc.'][i][j+1:]
			data1['Ref. / Doc.'][i]=float(data1['Ref. / Doc.'][i])
			#print(data1['SJR'][i],type(data1['SJR'][i]))
			break        

op=[]
op.append(np.array(data1['SJR'].astype('int').to_numpy()))
op.append(data1['H index'].to_numpy())
op.append(data1['Total Docs. (2017)'].to_numpy())
op.append(data1['Total Docs. (3years)'].to_numpy())
op.append(data1['Total Refs.'].to_numpy())
op.append(data1['Total Cites (3years)'].to_numpy())
op.append(data1['Citable Docs. (3years)'].to_numpy())
op.append(data1['Cites / Doc. (2years)'].astype('float64').to_numpy())
op.append(data1['Ref. / Doc.'].astype('float64').to_numpy())

opl=[]
for i in range(1,2**9):
    x=str(bin(i))
    x=x[2:]
    if x.count('1')>=2:
        while(len(x)<9):
            x='0'+x
        opl.append(x)

ans=[]
#p=[opl[0]]
#x3=[]
for i in range(len(opl)):
    #print(i)
    x2=[];
    for j in range(9):
        if opl[i][j]=='1':
            x2.append(op[j])
    #print(x2)        
    
    x3=np.array(x2[0])
    for j in range(1,len(x2)):
        x3=np.vstack((x3,x2[j]))
    #print(x3)
    ans.append(((error(x3,pred(x3))),i))

def s(x):
    return x[0]

ans.sort(key=s)
    