import numpy as np
import pandas as pd
import random

if __name__=="__main__":
    # kwargs = {"leaf_size": 1}
    # if "leaf_size" in kwargs:
    #     print " inside"
    #     print kwargs['leaf_size']
    # elif "ddd" in kwargs:
    #     print " ddd inside"
    # a = np.array([1,2,3,4])
    # b = a[a<1]
    # print b
    # # print b.shape[0]
    # a = []
    # for i in range(1,3):
    #     print i
    #     a.append(i)
    # a = np.array(a)
    # print a.mean()
    # x = np.array([[4, 2, 6], [5, 2, 7], [6, 2, 8]], np.int32)
    # row = np.random.choice(3, size= 3, replace=True)
    # print "row number: ", row
    # print x
    #
    # print "row for x",x[row]
    # x = x[:, 1:]
    # print x
    #
    # # y = np.mean(x, axis=1)
    # y = x[:,-1]
    # print y
    # print "row fir y", y[row]
    # print x[x[:, 0] < 6, : -1]
    # # print y[x[:, 0] < 6]
    # result = np.zeros((y.shape[0],))
    # for i in range(0,3):
    #     print i
    #     result = np.column_stack((result, y))
    # print result
    # print x.shape
    # print x
    # print y
    # print y.shape
    # print y.shape[0]
    #
    #
    # print np.isclose(y, y[0]).all()
    #
    # print "stack y to lower of x"
    # print np.vstack((x,y))
    #
    # print "stack y to right of x"
    # print np.column_stack((x, y))
    #
    # z = x[:, :-1]
    # print z
    # if np.isclose(z, z[0]).all():
    #     z = z[0]
    # print z

    # x = np.array([[1,2,3]])
    # print x.shape
    # print x.shape[0]
    # print x.shape[1]
    #
    # for i in range(0,9):
    #     # print i
    #     print random.randint(0, 3)

    # print np.random.choice(10, 10)

    # corr = []
    # for i in range(1,9):
    #     corr.append(i)
    # print corr
    # x = np.array(corr)
    # print x.shape
    # print x.max()
    # print x[x<8].max()
    # print np.argmax(x)

    # X = np.random.random(size=(50, 2)) * 200 - 50
    # print X

    # a = np.random.uniform(size=(3, 2))
    # b = a/a[1,:]
    # print a
    # print b

    # start_date = '2009-11-01'
#     # end_date = '2009-11-05'
#     # dates = pd.date_range(start_date, end_date)
#     # df1 = pd.DataFrame(index= dates)
#     # print df1

    # a = np.ones((4,4))
    # w = np.array([0.1,0.2,0.3,0.4])
    # print (a*w)
    # a= [1,2,3,4,5]
    # print a[0:4:3]
    # print a[-1]
    # a = np.random.randint(0,10, size=(5,5))
    # print a
    # print a[:, 1:4:1]
    # df1 = pd.DataFrame({'Type': ["stock", None]})
    # df2 = df1
    # print df2
    # df1.fillna("mutual fund", inplace=True)
    # print "=======after fillna"
    # print df2
    # df2.fillna("ETF", inplace=True)
    # print df1
    # print df2
    # w = np.array([3, 2, 5, 2, 1])
    # print w[: :-1]
    # df = pd.DataFrame(w, columns= ['numbers'], index = ['a','b', 'c','d','e'])
    # df = df.ix[df.index[2:5]].sum()
    # dr = df**2
    # print df
    #
    # data = { 'A':[100, 60, 30, np.nan],
    #          'B':[5, 15, 15, 5],
    #          'C': [100, 300, 100, 200],
    #          'D': [20, 20, 30, 30],
    #
    # }
    # df =pd.DataFrame(data)
    # print df
    # df = df.shift(-2)
    # print df

    # a= [[]] *4
    # a[1].add(15)
    # print a
    # i = [1,2,3,4,5]
    # print i[0:-1]
    # print i[0:4]
    # print i[0:4:1]
    # print i[0:4:2]
    # print i[0:4:3]
    # d = [(2, 2.5, 2.99, 3.5, 3.8, 10),
    #      (2, 2.5, 2.99, 3.5, 3.8, 10),
    #      (2, 2.5, 2.99, 3.5, 3.8, 10),
    #      (2, 2.5, 2.99, 3.5, 3.8, 10),
    #      (2, 2.5, 2.99, 3.5, 3.8, 10)]
    date =  pd.date_range(2008-10-1, 2008-10-5)
    df = pd.DataFrame(np.array([(1,2),(3,4),(5,6),(7,8), (9,0)]),index= date, columns= ['indicator1','indicator2'])
    print df
    # print df/df.shift(1)
    # data = np.ones([1,5])
    # print data
    # data[:, 2:4] = 0
    # print data
    # s = pd.DataFrame(data)
    # s.ix[:, 2:4] = 0
    # print s
    # print s.values
    # print s
    # print "========="
    # print s.size
    # print s.count()
    # m = np.arange(20).reshape(4,5)
    # print m
    # print m.sum(axis = 1)
    # print "====="
    # print m.cumsum(axis = 0)

    # for i in range(0, 4):
    #     a= random.randint(0,4)
    #     print "i: ", i
    #     print "a: ", a
    # random_list = np.random.randint(4, size=self.dyna)


