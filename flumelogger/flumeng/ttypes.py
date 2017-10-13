#
# Autogenerated by Thrift Compiler (0.9.3)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
# try:
#   from thrift.protocol import fastbinary
# except:
fastbinary = None


class Status:
  OK = 0
  FAILED = 1
  ERROR = 2
  UNKNOWN = 3

  _VALUES_TO_NAMES = {
    0: "OK",
    1: "FAILED",
    2: "ERROR",
    3: "UNKNOWN",
  }

  _NAMES_TO_VALUES = {
    "OK": 0,
    "FAILED": 1,
    "ERROR": 2,
    "UNKNOWN": 3,
  }


class ThriftFlumeEvent:
  """
  Attributes:
   - headers
   - body
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'headers', (TType.STRING,None,TType.STRING,None), None, ), # 1
    (2, TType.STRING, 'body', None, None, ), # 2
  )

  def __init__(self, headers=None, body=None,):
    self.headers = headers
    self.body = body

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.MAP:
          self.headers = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in range(_size0):
            _key5 = iprot.readString()
            _val6 = iprot.readString()
            self.headers[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.body = iprot.readString()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ThriftFlumeEvent')
    if self.headers is not None:
      oprot.writeFieldBegin('headers', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.headers))
      for kiter7,viter8 in self.headers.items():
        oprot.writeString(kiter7)
        oprot.writeString(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.body is not None:
      oprot.writeFieldBegin('body', TType.STRING, 2)
      oprot.writeString(self.body)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.headers is None:
      raise TProtocol.TProtocolException(message='Required field headers is unset!')
    if self.body is None:
      raise TProtocol.TProtocolException(message='Required field body is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.headers)
    value = (value * 31) ^ hash(self.body)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)