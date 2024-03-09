import ctypes
from ctypes.util import find_library

# Load libc, the C standard library
libc_name = find_library('c')
if not libc_name:
    raise EnvironmentError("Unable to find the C standard library.")

libc = ctypes.CDLL(libc_name)

# Size for an int
size = ctypes.c_size_t(ctypes.sizeof(ctypes.c_int))
# Allocate memory
ptr = libc.malloc(size)

# Confirm allocation success
if ptr == 0:
    raise MemoryError("Failed to allocate memory")

# Cast (void *) to (int *)
int_ptr = ctypes.cast(ptr, ctypes.POINTER(ctypes.c_int))

# Attempt to set the memory location pointed at by int_ptr to 42
# The following code would segfault
# int_ptr.contents.value = ctypes.c_int(42)

# We have to write with a raw ctype first before using this memory directly from py
int_ptr.contents = ctypes.c_int(0)
# Now this works!
int_ptr.contents.value = 42

print("Stored value:", int_ptr.contents.value)
