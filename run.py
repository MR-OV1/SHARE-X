import os, sys
try:
    __import__("s2").main()
except Exception as e:
    exit(str(e))
