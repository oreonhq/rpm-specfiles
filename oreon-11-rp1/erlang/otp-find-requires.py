#!/usr/bin/python3

# SPDX-FileCopyrightText: © 2026 Peter Lemenkov
# SPDX-License-Identifier: MIT

# RPM dependency generator for the subpackages of Erlang/OTP itself, using
# the multifile protocol. Every BEAM file of a subpackage requires the
# subpackages of the other OTP applications whose exported functions it
# calls, resolved against the buildroot:
#
#   erlang-APP(ISA) = VERSION-RELEASE
#
# Calls the compiler can't see (apply/3, rpc, module names computed at
# runtime) are deliberately not followed: OTP uses them for optional
# dependencies.
#
# Usage: otp-find-requires.py LIBDIR NAME VERSION-RELEASE [ISA]
#        otp-find-requires.py --spec ROOT
# The second form prints the Requires lines for the spec file, from an
# unpacked tree (a buildroot, or the RPMs extracted into ROOT).
#   LIBDIR is %{_libdir}/erlang/lib, NAME is %{name}, ISA is %{?_isa}

import functools
import glob
import os
import struct
import sys
import zlib

def chunks(filename):
	"""The chunks of a BEAM file, as {name: contents}."""
	with open(filename, "rb") as f:
		data = f.read()
	if data[:2] == b'\x1f\x8b':
		data = zlib.decompress(data, 31)
	result = {}
	pos = 12
	while pos + 8 <= len(data):
		name = data[pos:pos + 4]
		size = struct.unpack(">I", data[pos + 4:pos + 8])[0]
		result[name] = data[pos + 8:pos + 8 + size]
		pos += 8 + ((size + 3) & ~3)
	return result

def compact_length(data, pos):
	"""An atom length in the compact term encoding of OTP 28+."""
	b = data[pos]
	if b & 0x08 == 0:
		return b >> 4, pos + 1
	if b & 0x10 == 0:
		return ((b & 0xe0) << 3) | data[pos + 1], pos + 2
	n = (b >> 5) + 2
	return int.from_bytes(data[pos + 1:pos + 1 + n], "big"), pos + 1 + n

def atoms(c):
	data = c[b"AtU8"]
	count = struct.unpack(">i", data[:4])[0]
	pos = 4
	result = []
	for _ in range(abs(count)):
		if count < 0:
			size, pos = compact_length(data, pos)
		else:
			size, pos = data[pos], pos + 1
		result.append(data[pos:pos + size].decode())
		pos += size
	return result

def table(c, name):
	"""The entries of an import or export table, as tuples of 3 integers."""
	data = c[name]
	count = struct.unpack(">I", data[:4])[0]
	return [struct.unpack(">III", data[4 + 12 * i:16 + 12 * i]) for i in range(count)]

@functools.cache
def exports(filename):
	c = chunks(filename)
	a = atoms(c)
	return frozenset((a[f - 1], arity) for (f, arity, _) in table(c, b"ExpT"))

def imports(filename):
	c = chunks(filename)
	a = atoms(c)
	return {(a[m - 1], a[f - 1], arity) for (m, f, arity) in table(c, b"ImpT")}

def application(beam):
	"""The application a BEAM file belongs to: lib/APP-VSN/ebin/MOD.beam."""
	return os.path.basename(os.path.dirname(os.path.dirname(beam))).rsplit("-", 1)[0]

def requires(modules, filename):
	"""The other applications whose exported functions a BEAM file calls."""
	own = application(filename)
	result = set()
	for (m, f, a) in imports(filename):
		beam = modules.get(m)
		if beam and application(beam) != own and (f, a) in exports(beam):
			result.add(application(beam))
	return result

def index(libdir):
	return {os.path.basename(b)[:-5]: b for b in glob.glob(f"{libdir}/*/ebin/*.beam")}

def spec(root):
	"""Requires lines for the spec file, per application, from an installed tree."""
	libdir = glob.glob(f"{root}/usr/lib*/erlang/lib")[0]
	modules = index(libdir)
	apps = {}
	for beam in modules.values():
		apps.setdefault(application(beam), set()).update(requires(modules, beam))
	for app in sorted(apps):
		print(f"%package {app}")
		for dep in sorted(apps[app]):
			print(f"Requires: %{{name}}-{dep}%{{?_isa}} = %{{version}}-%{{release}}")

def main(argv):
	if argv[:1] == ["--spec"]:
		spec(argv[1])
		return
	(libdir, name, evr), isa = argv[:3], (argv[3] if len(argv) > 3 else "")
	root = os.environ.get("RPM_BUILD_ROOT", "").rstrip("/")
	modules = index(f"{root}{libdir}")

	for line in sys.stdin:
		filename = line.rstrip("\n")
		if not filename.endswith(".beam"):
			continue
		deps = requires(modules, filename)
		if deps:
			print(";" + filename)
			for app in sorted(deps):
				print(f"{name}-{app}{isa} = {evr}")

if __name__ == "__main__":
	main(sys.argv[1:])
