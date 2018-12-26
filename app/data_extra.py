from common.DbCommon import mysql2pd
import pandas as pd
import configparser,pickle
import numpy as np
def getdata():
    # conf_file='../common/db.conf'
    # conf = configparser.ConfigParser()
    # conf.read(conf_file)
    # conn=mysql2pd(conf.get('db','host'),conf.get('db','port'),conf.get('db','db'),conf.get('db','user'),conf.get('db','pwd'))
    # data=conn.doget("select * from beauty_markeup")
    # # print(data.columns)
    # conn.close()
    # with open('../data/ori_data.pkl','wb') as f:
    #     pickle.dump(data,f)
    with open('../data/ori_data.pkl','rb') as f:
        data=pickle.load(f)
    return data

def getDays(b='2018-11-01',e='2018-11-30'):
    date_index = pd.date_range(b,e)
    date_list = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in date_index.values]
    return pd.DataFrame(date_list,columns=['datetime'])

def data_tran():
    # data=getdata()
    # X=[]
    # Y=[]
    # for _, group in data.groupby('product_id'):
    #     if len(group)>5:
    #         b=min([pd.Timestamp(x[2]).strftime("%Y-%m-%d") for x in group.values])
    #         e=max([pd.Timestamp(x[2]).strftime("%Y-%m-%d") for x in group.values])
    #         data2=getDays(b,e)
    #         if len(data2.values)<30:
    #             pass
    #         else:
    #             group['datetime']=group['datetime'].apply(lambda x:pd.Timestamp(x).strftime("%Y-%m-%d"))
    #             data2=data2.merge(group,how='left',on='datetime')
    #             data2=data2.sort_values('datetime').fillna(method='pad')
    #             label=[]
    #             p_now=data2.values[0][3]
    #             for x in data2.values:
    #                 if p_now==x[3]:
    #                     label.append(2)
    #                 elif p_now>x[3]:
    #                     label.append(1)
    #                     p_now=x[3]
    #                 else:
    #                     label.append(0)
    #                     p_now=x[3]
    #             data2['label']=label
    #             one_X=[]
    #             one_Y=[0,0,0]
    #             for i,l in enumerate(data2.values):
    #                 if i<29:
    #                     one_X.append(float(l[3]))
    #                 elif i==29:
    #                     one_X.append(float(l[3]))
    #                     one_Y[l[4]]=1
    #                     X.append(np.array(one_X))
    #                     Y.append(np.array(one_Y))
    #                 else:
    #                     one_X.append(float(l[3]))
    #                     one_X.pop(0)
    #                     one_Y = [0, 0, 0]
    #                     one_Y[l[4]] = 1
    #                     X.append(np.array(one_X))
    #                     Y.append(np.array(one_Y))
    # print(len(X))
    # with open('../data/XY_data.pkl','wb') as f:
    #     pickle.dump((X,Y),f)
    with open('../data/XY_data.pkl','rb') as f:
        X,Y=pickle.load(f)
    return X[:100000],Y[:100000]
def data_load():
    X,Y=data_tran()
    batch_size=10
    data, label = np.array(X).astype(np.float32), np.array(Y)
    num_example = data.shape[0]
    ratio = 0.8
    cp = np.int(num_example * ratio)
    arr = np.arange(num_example)
    np.random.shuffle(arr)
    data = data[arr]
    label = label[arr]
    ratio = 0.8
    s = np.int(num_example * ratio)
    trX = data[:s]
    trY = label[:s]
    valX = data[s:]
    valY = label[s:]
    # num_tr_batch = cp // batch_size
    # num_val_batch = (num_example - cp) // batch_size
    return trX, trY,valX, valY
data_load()
