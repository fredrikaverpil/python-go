import ctypes
import platform

if platform.system() == "Linux":
    filename = "./fib.so"
elif platform.system() == "Darwin":
    filename = "./fib.dylib"
elif platform.system() == "Windows":
    filename = "./fib.dll"
else:
    err = OSError("Unknown system")
    raise err

so = ctypes.cdll.LoadLibrary(filename)

fib = so.fib
fib.argtypes = [ctypes.c_int]
fib.restype = ctypes.c_int

res: int = fib(10)
print(res)
