#!/usr/bin/python

import sys
import json
import dlutil
import caffe
from pprint import pprint
from subprocess import Popen, PIPE


class Model(object):
    def __init__(self, model_name, dataset_name):
        self.name = name
        self.dataset_name = dataset_name

    def write_train_net(self, batch_size):
        with open('self.dataset_name/lenet_auto_train.prototxt', 'w') as f:
            f.write(str(lenet('mnist/mnist_train_lmdb', batch_size)))

    def write_test_net(self, batch_size):
        with open('mnist/lenet_auto_test.prototxt', 'w') as f:
            f.write(str(lenet('mnist/mnist_test_lmdb', batch_size)))

    """def net(self, source, batch_size, net_layers=list()):
    # our version of LeNet: a series of linear and simple nonlinear transformations
        from caffe import layers as L, params as P
        n = caffe.NetSpec()
        n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=source,
                                     transform_param=dict(scale=1./255), ntop=2)

        for each_layer in net_layers:
            
        n.conv1 = L.Convolution(n.data, kernel_size=5, num_output=20, weight_filler=dict(type='xavier'))
    """ 



def get_model_hashtable():
        "Returns the model hashtable"
        dict={}
        p = Popen(["ls", "-1rt", MODEL_DIR_PATH], stdout=PIPE, bufsize=1)
        with p.stdout:
                for line in iter(p.stdout.readline, b''):
                        dir = line.strip();
                        minfo = read_json_file(MODEL_DIR_PATH + "/" + dir + "/.model")
                        dbname = minfo["modelName"]
                        mid   = minfo["id"]
                        dict[dbname] = mid
        p.wait() #wait for the subprocess to exit
        return dict;

def get_model_dir(mname):
        "Returns the directory where the named model is stored"
        p = Popen(["ls", "-1rt", MODEL_DIR_PATH], stdout=PIPE, bufsize=1)
        with p.stdout:
                for line in iter(p.stdout.readline, b''):
                        dir = line.strip();
                        minfo = read_json_file(MODEL_DIR_PATH + "/" + dir + "/.model")
                        dbname = minfo["modelName"]
                        if dbname == mname:
                                mdir   = minfo["modelDir"]
                                return mdir
        p.wait() #wait for the subprocess to exit
        return "";


def get_caffe_model_list():
	"return list o available topology models in caffe directory"
        p = Popen(["ls", "-1", CAFFE_MODEL_DIR_PATH], stdout=PIPE, bufsize=1)
        i=1
	dict = {}
        with p.stdout:
                for line in iter(p.stdout.readline, b''):
                        dir = line.strip()
			mpath = CAFFE_MODEL_DIR_PATH + "/" + dir
        		dict[dir] = mpath
                        i+=1
	p.wait() #wait for the subprocess to exit
        return dict;

def model_retrain(mname, options, inc_training_p, new_m_p):
	"retrain a model cold or warm, and save or create new copy"
	return;
 
def model_optimize(mname, options):
	"optimize model for deployment"
	return IRmname;
