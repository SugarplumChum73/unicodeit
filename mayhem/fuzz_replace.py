#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import unicodeit

def RandomString(fdp, min_len, max_len):
  str_len = fdp.ConsumeIntInRange(min_len, max_len)
  return fdp.ConsumeUnicodeNoSurrogates(str_len)

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    laexpr = RandomString(fdp, 0, 1000)
    
    unicodeit.replace(laexpr)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()