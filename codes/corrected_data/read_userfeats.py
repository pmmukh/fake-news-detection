import glob
import json
import os
import numpy as np
'''
f = open("userlist.txt","w")
idlist = []
for filename in glob.iglob('F:/Courses/NLP/proj/codes/corrected_data/*.txt'):
    try:
        jdat = json.load(open(filename))
        for x in jdat:
            newid = x["user"]["id"]
            if newid not in idlist:
                idlist.append(newid)
                f.write(str(newid)+"\n")
    except ValueError, ve:
        print(filename)
u = []
'''
u = []
num_events = 300
with open("userlist.txt","r") as userfile:
    users = userfile.readlines()
    u = [int(u.strip()) for u in users]
print(len(u))
incmat = np.zeros([len(u),num_events])
print(u)
i = 0
for filename in glob.iglob('F:/Courses/NLP/proj/codes/corrected_data/*.txt'):
    try:
        jdat = json.load(open(filename))

        print(filename)
        print("num of tweets " + str(len(jdat)))
        for x in jdat:
            newid = x["user"]["id"]
            j = i+1
            ind = u.index(newid)
            if incmat[ind][i] == 0:
                incmat[ind][i]=1

        i +=1
        print("event done for "+filename+"\n")
    except ValueError, ve:
        print(filename)
        print(ve)

u,s,vh = np.linalg.svd(incmat,full_matrices=False)
print(s.shape)
print(vh.shape)
en = [x*x for x in s]
torem = []
totalen = sum(en)
curr_en = totalen
toclip = len(s)
print("totalen is "+str(totalen))
for i in range(len(s)-1,-1,-1):
    curr_en -= s[i]*s[i]
    if curr_en>0.6*totalen:
        toclip=i
    else:
        print("curren is " + str(curr_en))
        break

print(toclip)
clipped_vt = vh[:toclip][:]

y = np.matmul(incmat,np.transpose(clipped_vt))
print(y.shape)
adjf = open("incmat_lowdim.txt","w")
for i in range(len(u)):
    adjf.write(",".join(str(x) for x in y[i])+"\n")

