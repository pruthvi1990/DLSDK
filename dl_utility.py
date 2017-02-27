#!/usr/bin/env python
###############################
# This program changes the hyper parameters in the *.solver.prototxt file
##############################

import os, sys
import re

def modify_learning_params(dataset_name, test_iter=100, test_interval=500, base_lr=0.01, momentum=0.9,   \
                            weight_decay=0.0005, lr_policy="inv", gamma=0.0001, power=0.75, \
                            display=100, max_iter=10000):
    
    args_dict = locals()
    
    with  open("/media/phthoreho/disk1/DLSDK/caffe/DLSDK_utilites/lenet_auto_solver.prototxt", 'r') as _file:
        buf = _file.readlines()
        for pos, item  in enumerate(buf):
            hyper_param = re.search(r'([\w_]+):', item)
            
            if hyper_param is not None:
                if hyper_param.group(1) in args_dict.keys():
                    buf[pos] = hyper_param.group() + " " + str(args_dict[hyper_param.group(1)]) + "\n"
    
    with open("/media/phthoreho/disk1/DLSDK/caffe/DLSDK_utilites/lenet_auto_solver.prototxt", 'w') as _file:
       _file.writelines(buf)

