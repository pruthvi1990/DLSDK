DLSDK_API function calls

General Utilities:
get_dlsdk_env():
	"return dlsdk environment variables"

get_dir_list(dirname):
	"Returns the dataset hashtable"

read_json_file (fname):
	"reads a json file and returns the info is a structure"	

write_json_file(data, fname):
	"Write a dictionary data in a json file"

wait_until_cmd (cmd, value):
	"wait until an os cmd returns value"

wait_until_not_cmd (cmd, value):
	"wait until an os cmd does not returns value"

wait_until_fe(fname):
	"wait until a file exists"

wait_until_not_fe(fname):
        "wait until a file does not exist"


Upload Utilities

list_uploaded_folders ():
	"list content of the DLSDK upload directory"

list_custom_uploaded_folders ():
	"list content of the custom uploaded files"

delete_uploaded_folder (fname):
	"remove uploaded data folder fromthe DLSDK upload direcyory"

delete_custom_uploaded_folder (fname):
	"remove uploaded data from the custom_upload directory"

upload_folder(scp_path_cred, remote_fname,  local_fname):
	"upload and unzip a data folder from another machine through scp" 


Label Utilities
get_labels_from_dir(fname, dict={}):
	"add contents of fname to label dictionary"

get_labels_from_file(fname, dict={}):
	"add contents of fname to label dictionary"

write_label_file(dict, fname):
	"write contents of dict to file"

merge_label_files(flabel1, flabel2, fdest):
	"merge label files stored in json or csv "

partition_label_file(flabel, trlabel, vallabel, testlabel, pctvec):
        "partition labels into 3 label files according to pct vector"


class MLABOptions():
      options = {}

      def __init__(self):
          return;

      defSetOption(self, key, val):
      	  return;
      def PrintOptions(self):
      	  return;
      def GetOptionValue(self, key):
      	  return val;

class MLABDatasetOptions(Options):
class MLABModelOptions(Options):
class MLABSolverOptions(Options):
class MLABLayerOptions(Options):


class MLABDataTransformer():
      width=0
      height=0
      channels=0
      name=[]
      syscall = []
      parameters = []
      def __init__(self):
      	  return;

      def Append(self, name, syscall, parameters):
      	  return;
      def Insert(self, pos, name, syscall, parameters):
          return;
      def Extend(self, xfm):
      	  return;

	  

class MLABDataSet():
      name=""
      dir=""
      lmdbname=""
      trpct=80;
      valpct=20;
      testpct=0;
      options = MLABDataSetOptions();
      xfm = MLABDataTransformer();

      def __init__(self):
      	  return;

      Print(self)
      Transform(self)
      Convert(self, labels, cwh=[3,0,0], fmt="lmdb")
      Create(self, labels, path)
      Append(self, ds)
      SetOption(self, key, value)
      

class MLABModel():
      name=""
      dir""
      
