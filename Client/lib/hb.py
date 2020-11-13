#
import gc
import os
import sys
from cat import *

def df():
    s = os.statvfs('//')
    ds = ('{0} KB'.format((s[0]*s[3])/1024))
    print('disk_free:\t%s'%ds)
    return ds

def mem_status():
    gc.collect()
    mf  = gc.mem_free()
    ma  = gc.mem_alloc()
    mt  = ma+mf
    mp  = '{0:.2f}%'.format(mf/mt*100)
    print("mem total/alloc/free:\t%d/%d/%d(%s)"%(mt,ma,mf,mp))
    return mt, ma, mf

def hb_status():
    mem_status()
    df()

def reload(mod):
    mod_name = mod.__name__
    del sys.modules[mod_name]
    return __import__(mod_name)

### 
if __name__ == "__main__":
    # execute only if run as a script
    hb_status()
