import base64
from typing import Union, cast

from Crypto.Cipher import AES


def to_bytes(raw: Union[str,bytes]) -> bytes:
  if type(raw) is str:
    return cast(str,raw).encode('utf-8')
  else:
    return cast(bytes,raw)

def to_ascii(raw: bytes) -> str:
  return raw.decode('ascii')

def to_hex(raw: bytes) -> str:
  return raw.hex()

def encode_Base64(raw: Union[str,bytes]) -> bytes:
  return base64.b64encode(to_bytes(raw))

def decode_Base64(encoded: Union[str,bytes]) -> bytes:
  return base64.b64decode(to_bytes(encoded))

def encode_AES_ECB(raw: Union[bytes,str], key: Union[bytes,str]) -> bytes:
  cipher = AES.new(to_bytes(key), AES.MODE_ECB)
  return cipher.encrypt(to_bytes(raw))

def decode_AES_ECB(encoded: bytes, key: bytes) -> bytes:
  cipher = AES.new(to_bytes(key), AES.MODE_ECB)
  return cipher.decrypt(to_bytes(encoded))

def add_padding(raw: str, char: str, padding: int) -> str:
  """rawをパディングに合うように後ろにcharを詰める
  
  Arguments:
      raw {str} -- もともと
      char {str} -- 詰めるときに使う文字
      padding {int} -- パディング長
  
  Returns:
      str -- 長さがパディングの倍数となった結果
  """

  return raw + char * (padding - (len(raw) % padding))
