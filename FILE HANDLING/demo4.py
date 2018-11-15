import os.path as pa
fname=input("enter file name wit ext:")
res=pa.exists(fname)
if res:
    f=open(fname)
    s=f.read()
    print(s)
    f.close()
else:
     print("file is not found")