#!/usr/bin/python

import sys
import dlutil as du

env = du.get_dlsdk_env()
caffe_root = env["CAFFE_DIR"]
sys.path.insert(0, caffe_root + 'python')
import caffe


#def set_caffe_path():
#	"setup caffe and add it to the path"
#        env = du.get_dlsdk_env();
#        caffe_root = env["CAFFE_ROOT"]
#        sys.path.insert(0, caffe_root + 'python')
#	return;

def get_caffe_version():
    return caffe__version__ ;


