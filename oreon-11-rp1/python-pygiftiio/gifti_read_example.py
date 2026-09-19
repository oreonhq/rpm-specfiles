from pygiftiio import *
import numpy

# Read Gifti Image
filename = '/path/to/file'
image = gifti_read_image(fn, 1)

# image is now of type GiftiImage
# The _fields_ variable is populated with the same structure
# as the C-based struct
# Now we query the image to get data arrays, meta data, etc.
print "Number of Data Arrays in Image = " + str(image.numDA)

# Extract a dataarray from the Gifti Image based on its index.
def get_da_from_index(im, ind):
    if ind = im.numDA:
        print "Index exceeds number of DA's in gifti image"

    # Most things are handled automatically by the ctypes wrapping.
    # However, in the case of pointers, you need to access the
    # contents of the pointer to get the right result
    return im.darray[ind].contents

# Extract a dataarray from the Gifti Image based on its IntentCode
def get_da_from_intent(im, intent):
    for i in xrange(im.numDA):
        # Intent code is stored in the DataArray struct
        da = im.darray[i].contents

        # The wrapping allows the intent codes to be represented as
        # integers as defined by the C-Macros or as the strings that
        # are replaced.
        if type(intent) == type(1):
            if da.intent == intent:
                # Grab the first DataArray that is the correct intent
                return da
        else:
            # If it's not an int, we have to look up the integer value in
            # the Intent Code dictionary
            if da.intent == GiftiIntentCode.intents[intent]:
                return da

# Extract metadata from the GiftiImage OR a GiftiDataArray 
def get_metadata_from_image(im):
    metadata = im.meta
    # metadata is now of type GiftiMetaData.  It has length, name, and value arrays.
    return metadata

# Print all the metadata in the GiftiMetaData object
def print_metadata(md):
    size = md.length
    for i in xrange(size):
        name = md.name[i]
        val = md.value[i]
        print str(name) + ": " + str(val)

# Extract the Coordinate Transform(s) from a dataarray
def get_coord_xform(da):
    dspace = da.coordsys.contents.dataspace
    xformspace = da.coordsys.contents.xformspace
    xform = da.coordsys.contents.xform
    xform_ar = numpy.array(xform) # make the list of values into an array
    xform_ar.shape = 4,4          # reshape the array into a valid transform matrix
    return xform_ar               # Return a numpy array representing the transform


