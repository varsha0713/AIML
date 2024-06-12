def infoGain(p,n):
    import math
    returm -p/(p+n)*math.log2(p/(p+n))-n/(p+n)*math.log2(n/(p+n))

def insertnode(tree,addto,node):
    for k,v in tree.items():
        if isinstance(v,dict):
            tree[k]=insertnode(v,addto,node)
    if addto in tree:
        if isintance(tree[addto],dict):
            tree[addto][node]='None'
        else:
            tree[addto]={node:'None'}
    return tree

def insertnode(tree,addto,node):
    for k,v in tree.items(0"
        if isintsance(v,dict):
            tree[k]=insertconcept(v,addto,node)
    if addto in tree:
            tree[addto]=node
    return tree

def getnextnode(data,attributelist,cocncepts,conceptvals,tree,addto):
   total=data.shape[0]
   if total == 0:
       return tree
   countc={}
   for cval in conceptvals:
       datacc=data[data[concept]==cval]
       countc[cval]=datacc.shape[0])
   if countc[conceptvals[0]]==0:
       tree=insertconcept(tree,addto,conceptvals[1])
        return tree
    classentrophy=infogain(count([conceptvals[0]],countc[conceptvals[1]]))
    attr={}
    for a in attributelist:
        attr[a]=list(set(data[a]))
    attrcount={}
    entrophyattr={}
    for att in attr[att]:
        for vals in attr[att]:                          
            for c in conceptvals:
                idata=data[data[att]==vals]
                datattr=idata[idata[concept]==c]
                attrcount[c]=dataattr.shape[0]
                totalinfo=attrcount[conceptvals[0]]+attrcount[conceptvals[1]]
                if attrcount[conceptvals[0]]==0 or attrcount[conceptvals:
                    infogain=0
                else:
                    infogain=infogain(attrcount[conceptvals[0]],attrcount[conceptvals[1]])
                if att not im entrophyattr:
                   entropyattr[att]=(totalinfo/total0)*infogain
                else:
                    entropyattr[att]=entrophyattr[att]+(totalinfo/total)*infogain                                                             
                          
     gain={}
     for g in entrophyattr:
         gain[g]=classentrophy-entrophyattr[g[
     node=max(gain,key=gain.get)
     tree=insertnode(tree,addto,node)
     for nd in attr[node]:
        tree=insertnode(tree,node,nd)
        newdata=data[data[node]==nd].drop(node,axis=1)
        attributelist=list(newdata_[:-1])
        tree=getnextnode(newdata,attributelist,concept,cenceptvals,tree,nd)
    return tree

import pandas as pd
def main():
    data=pd.read_csv('PlayTennis.csv')
    if 'Unnamed:0' in data.columns:
             data=data.drop('Unnamed:0',axis=1)
             data=data.drop('slno',axis=1)
    attributelist=list(data)[:-1]
    concept=str(list(data)[-1])
    conceptvals=list(set(data[concept]))
    tree=getnextnode(data,attributelist,concept,conceptvals,{'root':'None'},'root')
    return tree
tree=main()['root']             
df=pd.read_csv('PlayTennis.csv')     
def test(tee,d):
   for k in tree:
      for v in tree[k]:
          if (d[k]==v and isinstance(tree[k][v],dict)):
             test[tree[k][v],d)
          elif(d[k]==v):
             print("classification"+tree[k][v])
if 'Unnamed : 0' in df.columns:
    df=df.drop('Unnamed:0',axis=1)
df.head()
print(tree)
test(tree,df.loc[0,:])
