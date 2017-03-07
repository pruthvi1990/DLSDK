#!/usr/bin/python

import sys
import json
import dlutil

from pprint import pprint
from subprocess import Popen, PIPE

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
