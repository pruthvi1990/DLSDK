#!/usr/bin/python

import os
import json
import csv
from subprocess import Popen, PIPE

from pprint import pprint


#commented for testing only
def get_dlsdk_env():
	"return dlsdk environment variables"
	env = {};
	env["UPLOAD_DIR"]       = "/workspace/dlsdk/uploads/"
	env["CUSTOM_UPLOAD_DIR"]= "/workspace/dlsdk/custom_uploads/"
	env["DATASET_DIR"]      = "/workspace/dlsdk/jobs/datasets/"
	env["CUSTOM_DATASET_DIR"]= "/workspace/dlsdk/jobs/custom_datasets/"
	env["MODEL_DIR"]        = "/workspace/dlsdk/jobs/models/"
	env["CUSTOM_MODEL_DIR"] = "/workspace/dlsdk/jobs/custom_models/"
	env["TOOL_DIR"]         = "/opt/dlsdk/"
	env["CAFFE_DIR"]        = "/opt/caffe/"
	env["MODEL_OPTIMIZER_DIR"] = (env["TOOL_DIR"] + 
				      "model-optimizer/")
	env["CAFFE_MODEL_DIR_PATH"] = "tbd"
	return env;

def get_dir_list(dirname):
	"Returns the dataset hashtable"
	dlist = list()
	p = Popen(["ls", "-1a", dirname], stdout=PIPE, bufsize=1)
	with p.stdout:
		for line in iter(p.stdout.readline, b''):
			fname = line.strip();
			dlist.append(fname)
	p.wait() #wait for the subprocess to exit
	return dlist;

def read_json_file (fname):
	"this function reads a json file and returns the info is a structure"	
	with open(fname) as data_file:    
		data = json.load(data_file)
	return data;

def write_json_file(data, fname):
	"Write a dictionary data in a json file"
	with open(fname, 'w') as f:
		json.dump(data, f)
	return;
    
def wait_until_cmd (cmd, value):
	"wait until an os cmd returns value"
	while os.system(cmd) != value:
		os.system("sleep 1") 
	return;

def wait_until_not_cmd (cmd, value):
	"wait until an os cmd does not returns value"
	while os.system(cmd) == value:
		os.system("sleep 1") 
	return;

def wait_until_fe(fname):
	"wait until a file exists"
	while os.access(fname, os.F_OK) == False:
		os.system("sleep 1") 
	return;

def wait_until_not_fe(fname):
        "wait until a file does not exist"
        while os.access(fname, os.F_OK) == True:
                os.system("sleep 1") 
        return;

def list_uploaded_folders ():
	"list content of the DLSDK upload directory"
	env = get_dlsdk_env()
	cmd = "ls -al " + env[UPLOAD_DIR]
	if (os.system(cmd) != 0) :
		print("Error: Unable to run: "+cmd)
	return;

def list_custom_uploaded_folders ():
	"list content of the custom uploaded files"
	env = get_dlsdk_env()
	cmd = "ls -al " + env[CUSTOM_UPLOAD_DIR]
	if (os.system(cmd) != 0) :
		print("Error: Unable to run: "+cmd)
	return;

def delete_uploaded_folder (fname):
	"remove uploaded data folder fromthe DLSDK upload direcyory"
	env = get_dlsdk_env()
	cmd = "rm -fr "+ env[UPLOAD_DIR] + fname
	if (os.system(cmd) != 0):
		print("Error: Unable to run: "+cmd)
	return;

def delete_custom_uploaded_folder (fname):
	"remove uploaded data from the custom_upload directory"
	env = get_dlsdk_env()
	cmd = "rm -fr "+ env[CUSTOM_UPLOAD_DIR] + fname
	if (os.system(cmd) != 0):
		print("Error: Unable to run: "+cmd)
	return;

def upload_folder(scp_path_cred, remote_fname,  local_fname):
	"upload and unzip a data folder from another machine through scp" 
	env = get_dlsdk_env()
	cmd = "scp "+scp_path_creed+":"+fname+" "+env[UPLOAD_DIR]+local_fname
	if os.system(cmd) != 0:
		print("Error: Unable to run: " + cmd)
		return
	sl = remote_fname.split(".")
	ll = len(sl)
	if (ll >1):
		ext = ls[ll-1]
		if (ext == "gzip"):
			cmd = "gunzip "+ env[UPLOAD_DIR]+local_fname
		elif (ext == "rar"):
			cmd = "unrar x "+ env[UPLOAD_DIR]+local_fname
		else:
			cmd = ""
		if (os.system(cmd) != 0):
			print("Error: Unable to run: "+cmd)
		return;


def get_labels_from_dir(fname, dict={}):
	"add contents of fname to label dictionary"
	fs = fname.split("/")
	label = fs[len(fs)-1]
	print("label = " + label)
	for root, dirs, files in os.walk(fname, topdown=False):
		print("root = "+str(root))
		for name in files:
			print("file = " + name)
			dict[os.path.join(root, name)] = label
		for name in dirs:
			print("dir = " + os.path.join(root, name))
			get_labels_from(os.path.join(root, name), dict)
	return dict;


def get_labels_from_file(fname, dict={}):
	"add contents of fname to label dictionary"

	sl = fname.split(".")
	ll = len(sl)
	if (ll >1):	  
		ext1= sl[ll-1]
	else:
		ext1=""
		print(ext1)
	if (ext1 == "csv"):
		with open(fname, "rb") as csvfile:
			reader = csv.reader(csvfile, dialect = 'excel')
			for row in reader:
				dict[row[0]] = row[1]
	elif (ext1 == "json"):
		dict2 = read_json_file(fname)
		dict.update(dict2)
	else:
		print("unknown extension for file: " + fname)
	return dict;
			      
			      
def write_label_file(dict, fname):
	"write contents of dict to file"

	sl = fname.split(".")
	ll = len(sl)
	if (ll >1):	  
		ext1= sl[ll-1]
	else:
		ext1=""
	if (ext1 == "csv"):
		with open(fname, "wb") as csvfile:
			writer = csv.writer(csvfile, dialect = 'excel')
			keys = dict.keys();
			for k in keys:
				writer.writerow([k, dict[k]])
				
	elif (ext1 == "json"):
		write_json_file(dict, fname)
	else:
		print("unknown extension for file: " + fname)
	return dict;

		      
def merge_label_files(flabel1, flabel2, fdest):
	"merge label files stored in json or csv "

	dict1 = get_labels_from_file(flabel1)
	dict2 = get_labels_from_file(flabel2)
	dict1.update(dict2)
	write_label_file(dict1, fdest);
	return;    


def partition_dataset (label_file, tr_pct, val_pct, \\
		       tr_label, val_label, test_label):
	"divide training data into tr, val, and test datasets"
	return tlabel, vlabel, tstlabel;


