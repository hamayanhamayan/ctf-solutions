import requests
from typing import Dict
from typing import Union, cast
import base64
import time
import binascii
import urllib.parse
import hashlib

import percache
cache = percache.Cache('util')

lasttime = None

def get_file_via_internet_without_cache(url: str, params: Dict[str, str], cookie: Dict[str, str] = {}) -> str:
  global lasttime

  if lasttime != None:
    d = 1 - (time.time() - lasttime)
    if 0 < d:
      time.sleep(d)

  req = requests.Request('GET', url, params=params, cookies=cookie)
  prepared = req.prepare()
  session = requests.Session()
  res = session.send(prepared, allow_redirects = True)
  lasttime = time.time()
  return res.content.decode("utf-8")

@cache
def get_file_via_internet(url: str, params: Dict[str, str], cookie: Dict[str, str] = {}) -> str:
  global lasttime

  if lasttime != None:
    d = 1 - (time.time() - lasttime)
    if 0 < d:
      time.sleep(d)

  req = requests.Request('GET', url, params=params, cookies=cookie)
  prepared = req.prepare()
  session = requests.Session()
  res = session.send(prepared, allow_redirects = True)
  lasttime = time.time()
  return res.content.decode("utf-8")


@cache
def get_file_via_internet(url: str, params: Dict[str, str]) -> str:
  global lasttime

  if lasttime != None:
    d = 1 - (time.time() - lasttime)
    if 0 < d:
      time.sleep(d)

  req = requests.Request('GET', url, params=params)
  prepared = req.prepare()
  session = requests.Session()
  res = session.send(prepared, allow_redirects=True)
  lasttime = time.time()
  return res.content.decode("utf-8")

@cache
def get_file_via_internet_post_form(url: str, params: Dict[str, str]) -> str:
  global lasttime

  if lasttime != None:
    d = 1 - (time.time() - lasttime)
    if 0 < d:
      time.sleep(d)

  req = requests.Request('POST', url, data=params)
  prepared = req.prepare()
  session = requests.Session()
  res = session.send(prepared, allow_redirects=False)
  lasttime = time.time()
  return res.content.decode("utf-8")

def get_file_via_internet_post_form_nocache(url: str, params: Dict[str, str]) -> str:
  global lasttime

  if lasttime != None:
    d = 1 - (time.time() - lasttime)
    if 0 < d:
      time.sleep(d)

  req = requests.Request('POST', url, data=params)
  prepared = req.prepare()
  session = requests.Session()
  res = session.send(prepared, allow_redirects=False)
  lasttime = time.time()
  return res.content.decode("utf-8")

def to_bytes(raw: Union[str, bytes]) -> bytes:
  if type(raw) is str:
    return cast(str, raw).encode('utf-8')
  else:
    return cast(bytes, raw)

def to_ascii(raw: bytes) -> str:
  return raw.decode('ascii')

def to_hex(raw: bytes) -> str:
  return raw.hex()

def to_hex(raw: int) -> str:
  return '{:02x}'.format(raw)

def to_base64(raw: bytes) -> str:
  return to_ascii(base64.b64encode(raw))

def to_base64(raw: str) -> str:
  return to_ascii(base64.b64encode(to_bytes(raw)))

def from_base64(raw: str) -> bytes:
  while len(raw) % 4 != 0:
    raw += '='
  return binascii.a2b_base64(to_bytes(raw))

def from_url(raw: str) -> str:
  return urllib.parse.unquote_plus(raw)

def to_url(raw: str) -> str:
  return urllib.parse.quote_plus(raw)

def to_md5(raw: str) -> str:
  return hashlib.md5(raw.encode('utf-8')).hexdigest()
