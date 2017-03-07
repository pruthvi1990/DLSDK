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
      
