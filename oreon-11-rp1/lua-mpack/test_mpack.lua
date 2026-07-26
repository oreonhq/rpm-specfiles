local mpack = require('mpack')

local t = mpack.unpack('\100')

local obj = {
    k1 = {
        {
            k2 = {{{{{{{{{{{{{{{{{{{{{{{{{{{{{1}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
        }
    }
}
local unpack = mpack.Unpacker()
local pack = mpack.Packer()
local o = unpack(pack(obj))
