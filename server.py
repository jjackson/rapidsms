#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import sys
import os
#os.environ["PYTHONPATH"] = os.path.join(os.getcwd(),'lib')
sys.path.append(os.path.join(os.getcwd(),'lib'))
    
import rapidsms

if __name__ == "__main__":
    rapidsms.manager.start(sys.argv)
