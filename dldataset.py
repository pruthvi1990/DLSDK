#!/usr/bin/python

import os
import dlutil as du
from subprocess import Popen, PIPE


def get_dataset_hashtable():
    "Returns the dataset hashtable"
    dict={}
    env = du.get_dlsdk_env()
    p = Popen(["ls", "-1rt", env["DATASET_DIR"]], stdout=PIPE, bufsize=1)
    with p.stdout:
        for line in iter(p.stdout.readline, b''):
            dir = line.strip();
            dsinfo = du.read_json_file(env["DATASET_DIR"] + \
                                           dir + "/.dataset")
            dbname = dsinfo["dbName"]
            dsid   = dsinfo["datasetID"]
            dict[dbname] = dsid
    p.wait() #wait for the subprocess to exit
    return dict;


def get_dataset_dir(dsname):
    "Returns the directory where the named dataset is stored"
    env = du.get_dlsdk_env()
    p = Popen(["ls", "-1rt", env["DATASET_DIR"]], stdout=PIPE, bufsize=1)
    with p.stdout:
        for line in iter(p.stdout.readline, b''):
            dir = line.strip();
            dsinfo = du.read_json_file(env["DATASET"] + \
                                           dir + "/.dataset")
            dbname = dsinfo["dbName"]
            if dbname == dsname:
                dsdir   = dsinfo["datasetDirectory"]
                return dsdir
            p.wait() #wait for the subprocess to exit
    return "";


def get_dataset_files(dsname, dirname=""):
    "Get a list of all dataset files"
    if (dirname == ""):
        dirname= get_dataset_dir(dsname)
    ds = {};
    ds["name"] = dsname
    ds["directory"] = dirname
    dlist = du.get_dir_list(dirname)
    ds["files"] = dlist
    if (".dataset" in dlist):
        ds["dsinfo"] = os.path.join(dirname, ".dataset")
    else:
        ds["dsinfo"] = ""
    return ds;


def create_training_dataset(labeldict, lmdbname, options):
    "Create a dataset from an uploaded folder and store it in dest"
    ds = {};
    return (ds);

def create_inference_dataset(fname, dest, options):
    "Create a dataset from an uploaded folder and store it in dest"
    ds = 0;
    return (ds, labels);

def add_to_training_dataset(dsname, newdatapath, new_ds_p):
	"add images and labels to dataset, and replace or create new copy"
	return;

def add_to_inference_dataset(dsname, newdatapath, new_ds_p):
	"add images and labels to dataset, and replace or create new copy"
	return;

