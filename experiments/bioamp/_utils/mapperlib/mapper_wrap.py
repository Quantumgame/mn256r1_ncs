# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mapper_wrap', [dirname(__file__)])
        except ImportError:
            import _mapper_wrap
            return _mapper_wrap
        if fp is not None:
            try:
                _mod = imp.load_module('_mapper_wrap', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mapper_wrap = swig_import_helper()
    del swig_import_helper
else:
    import _mapper_wrap
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def die(*args):
  return _mapper_wrap.die(*args)
die = _mapper_wrap.die

def programMemoryRange(*args):
  return _mapper_wrap.programMemoryRange(*args)
programMemoryRange = _mapper_wrap.programMemoryRange

def programMemory(*args):
  return _mapper_wrap.programMemory(*args)
programMemory = _mapper_wrap.programMemory

def programBulkSpec(*args):
  return _mapper_wrap.programBulkSpec(*args)
programBulkSpec = _mapper_wrap.programBulkSpec

def programDetailMapping(*args):
  return _mapper_wrap.programDetailMapping(*args)
programDetailMapping = _mapper_wrap.programDetailMapping

def programAddressRange(*args):
  return _mapper_wrap.programAddressRange(*args)
programAddressRange = _mapper_wrap.programAddressRange

def programOffset(*args):
  return _mapper_wrap.programOffset(*args)
programOffset = _mapper_wrap.programOffset
# This file is compatible with both classic and new-style classes.


