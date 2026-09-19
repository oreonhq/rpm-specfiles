from pygiftiio import *
from ctypes import *
import numpy

# setup
image = GiftiImage()
# CTypes provides constructors for pointer-based types.  This is important
# to the initialization of the various members of the structs we need
# to write via the library.
image.version = c_char_p("version_string")
image.darray = POINTER(POINTER(GiftiDataArray))()
image.data = c_void_p(None)
image.numDA = c_int(0)
image.swapped = c_int(0)
image.compressed = c_int(0)

# type(im) = GiftiImage
# type(ver) = str
def set_version(im, ver):
    image.version = c_char_p(ver)

# type(im) = GiftiImage
# type(numDA) = int
def set_numDA(im, numDA):
    im.numDA = c_int(numDA)

# type(im) = GiftiImage
# type(md) = GiftiMetaData
def set_meta_data(im, md):
    im.meta = md

# type(im) = GiftiImage
# type(da) = GiftiDataArray
def add_data_array(im, da):
    cur_numda = im.numDA

    # Create a pointer to the new dataarray
    da_ptr = pointer(da.data)
    # Grab the pointer to the image's dataarrays
    ptr = image.darray

    # Create a new dataarray array pointer
    ar = (POINTER(GiftiDataArray)*(cur_numda+1))()
    # We need to cast the resulting pointer for use by C
    ar = cast(ar, POINTER(POINTER(GiftiDataArray)))

    # Copy all of the current da's to the new array.  This just copies the pointers!
    for i in xrange(num_da):
        ar[i] = im.darray[i]

    # Add the new data array to the image's data
    ar[num_da] = da_ptr

    # Reassign the pointer
    im.darray = ar

    # Tell the image it has an extra DA now
    cur_numda += 1
    im.numDA = c_int(cur_numda)

# type(da) = GiftiDataArray
# type(axis) = int
# type(val) = int
def set_da_dim(da, axis, val):
    # Simple setter.  However, the axis variable here is a
    # python array index (as the da dims is an array)
    # To properly assign the value, the val variable must
    # be usable by C, so we must form a c_int type.
    # This is true for all Setters.
    da.dims[axis] = c_int(val)

# type(filename) = string
# type(im) = GiftiImage
def write_image(filename, im):
    return gifti_write_image, im, filename, 1)
