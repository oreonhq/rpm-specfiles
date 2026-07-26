%global source0_hash 8b642127880e92e8a75400125307724635ecdf4020ca4481e5efe7640451bb92

# Copyright (c) 2015, 2016  Dave Love, University of Liverpool
# Copyright (c) 2018  Dave Love, University of Manchester
# MIT licence, per Fedora policy

# Notes:
# The specific compiler flags used are presumably chosen sensibly for the
# code, and there's no likely security implication for this.

# ix86 isn't built -- see
# https://github.com/hfp/libxsmm/issues/103#issuecomment-256887962

# For historical reasons, these have been out of step with the ABI
# versioning used by the base source.  The soversion reflects the stable
# "base" functionality, while the rest is considered unstable upstream.
%global somajor 1
%global sominor 10
%global soupd 1

# Avoid FTBFS with gcc 15 https://github.com/libxsmm/libxsmm/issues/933
%global optflags %optflags -std=gnu17

Name:		libxsmm
Version:	1.17
Release:	8%{?dist}
Summary:	Small dense or sparse matrix multiplications and convolutions for x86_64
License:	BSD-3-Clause
URL:		https://github.com/hfp/libxsmm
Source0:	https://github.com/hfp/libxsmm/archive/%version/%name-%version.tar.gz
# Remove rpath
Patch0:		libxsmm-rpath.patch
BuildRequires:	make
BuildRequires:	python3-devel openblas-devel
BuildRequires:	gcc-gfortran gcc-c++
ExclusiveArch:	x86_64

# Remove /bin/sh, /bin/bash dependencies from -doc (not actually
# required by packaging guidelines)
%global __requires_exclude /bin/.*sh$
%{?filter_setup:
%filter_from_requires /\/bin\/.*sh$/d
%filter_setup
}

%description
LIBXSMM is a library for small dense and small sparse matrix-matrix
multiplications, as well as for deep learning primitives such as small
convolutions targeting Intel Architecture (x86).  The library
generates code for the following instruction set extensions: Intel
SSE, Intel AVX, Intel AVX2, IMCI (KNCni) for Intel Xeon Phi
coprocessors ("KNC"), and Intel AVX‑512 as found in the Intel Xeon Phi
processor family ("KNL") and future Intel Xeon processors.  Small
convolutions are currently only optimized for Intel AVX‑512.
Historically the library was solely targeting the Intel Many
Integrated Core Architecture "MIC") using intrinsic functions.
Currently, optimized assembly code targets all aforementioned
instruction set extensions (static code generation), and Just‑In‑Time
(JIT) code generation targets Intel AVX and beyond.

%package	devel
Summary:	Development files for %name
Requires:	%name%{?_isa} = %version-%release
Requires:	pkgconfig

%description	devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package	doc
Summary:	Documentation for %name
BuildArch:	noarch

%description	doc
Documentation for %name.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# MS-Windows stuff that rpmlint would complain about
find samples -name \*.vcxproj | xargs rm
# README would clobber the main one, and the others would be dangling links
rm documentation/{README,LICENSE,CONTRIBUTING}.md

# documentation/gxm.md is a symlink, wrong when the doc is installed.
rm documentation/gxm.md
cp -p samples/deeplearning/gxm/README.md documentation/gxm.md

%build
# OpenMP is only used by libxsmmext, so no need to turn it off.
# Avoid the ld hardening flags, which are taken care of by the library
# build system to the extent they don't affect perfromance.
# -lm and -ldl are neded for the test, for which the LDFLAGS need to be
# consistent.  PREFIX and POUTDIR are needed at build time to get the .pc
# files correct.  OMPLIB is necessary to avoid failure in epel7 trying to
# link -lgomp.so, which I haven't figured out.
%global makeflags STATIC=0 SYM=1 AVX=0 PYTHON=%python3 PREFIX=%_prefix POUTDIR=%_lib PPKGDIR=%_lib/pkgconfig VERSION_API=1 OMPLIB=-lgomp
%make_build %makeflags

%install
# Supply STATIC etc. since this actually builds stuff (a bug?),
# and otherwise we end up with bits built wrongly.
%make_install %makeflags
mkdir -p %buildroot%_fmoddir %buildroot%_libdir/pkgconfig
mv %buildroot%_includedir/libxsmm.mod %buildroot%_fmoddir
rm -r %buildroot%_datadir/libxsmm

# Build artefacts
find samples -name .make | xargs rm
cp Makefile.inc samples		# included by the sub-directories
echo "These are set up to be built in the original source tree.
You will have to adjust the make files to use an installed version." >samples/README

%check
# Fixme: the test gives numerical errors inconsistently with openblas
# 0.3.1/gcc 8.1 on koji when the thread count isn't 1; sometimes 2
# works.
OMP_NUM_THREADS=1 make test-cp2k %makeflags
rm -r samples/cp2k/{.make,.state,cp2k-dbcsr,cp2k-collocate,cp2k-test.txt}
# For some reason this only seems necessary for el8
rm -rf samples/cp2k/obj

%ldconfig_scriptlets

%files
%license LICENSE.md
%_libdir/libxsmm*.so.%{somajor}*

%files devel
%doc README.md
%_libdir/libxsmm*.so
%_includedir/*
%_bindir/libxsmm_gemm_generator
# Get the module directory owned.  Currently in Fedora, gfortran owns
# %%_fmoddir, but not %%_fmoddir/..
%_fmoddir/libxsmm.mod
%_libdir/pkgconfig/*.pc

%files doc
%doc README.md documentation/*.md documentation/*.pdf samples CONTRIBUTING.md
%license LICENSE.md

%changelog
%autochangelog
