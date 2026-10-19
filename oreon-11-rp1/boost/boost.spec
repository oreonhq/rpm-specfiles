%global source0_hash 5c1d40cb8e19adbf740a4ec2da35b3e58f3f5804b1dce44deb53df72193cbc6c
%global boost_docdir __tmp_docdir
%global boost_examplesdir __tmp_examplesdir
%if 0%{?flatpak}
%bcond_with mpich
%bcond_with openmpi
%else
%bcond_with mpich
%bcond_with openmpi
%bcond_with check
%endif
%ifnarch %{ix86} x86_64 %{arm} ppc64 ppc64le aarch64 s390x riscv64
  %bcond_with context
%else
  %bcond_without context
%endif
%bcond_without python3
%ifnarch %{ix86} x86_64
  %bcond_with quadmath
%else
  %bcond_without quadmath
%endif
%ifnarch x86_64
  %bcond_with stacktrace_from_exception
%else
  %bcond_without stacktrace_from_exception
%endif
Name: boost
%global real_name boost
Summary:        The free peer-reviewed portable C++ source libraries
Version: 1.92.0
Release:        1%{?dist}
License: BSL-1.0 AND MIT AND Python-2.0.1
%global version_enc %{lua:
  local ver = rpm.expand("%{version}")
  ver = ver:gsub("%.", "_")
  print(ver)
}
%global toplev_dirname %{real_name}_%{version_enc}
URL: http://www.boost.org
Source0:        https://archives.%{name}.io/release/%{version}/source/%{name}_1_92_0.tar.bz2
Source1:        b2.1
%global sonamever %{version}
Requires: %{name}-atomic%{?_isa} = %{version}-%{release}
Requires: %{name}-charconv%{?_isa} = %{version}-%{release}
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Requires: %{name}-cobalt%{?_isa} = %{version}-%{release}
Requires: %{name}-container%{?_isa} = %{version}-%{release}
Requires: %{name}-contract%{?_isa} = %{version}-%{release}
%if %{with context}
Requires: %{name}-context%{?_isa} = %{version}-%{release}
Requires: %{name}-coroutine%{?_isa} = %{version}-%{release}
%endif
Requires: %{name}-date-time%{?_isa} = %{version}-%{release}
%if %{with context}
Requires: %{name}-fiber%{?_isa} = %{version}-%{release}
%endif
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires: %{name}-graph%{?_isa} = %{version}-%{release}
Requires: %{name}-iostreams%{?_isa} = %{version}-%{release}
Requires: %{name}-json%{?_isa} = %{version}-%{release}
Requires: %{name}-locale%{?_isa} = %{version}-%{release}
Requires: %{name}-log%{?_isa} = %{version}-%{release}
Requires: %{name}-math%{?_isa} = %{version}-%{release}
Requires: %{name}-nowide%{?_isa} = %{version}-%{release}
Requires: %{name}-process%{?_isa} = %{version}-%{release}
Requires: %{name}-program-options%{?_isa} = %{version}-%{release}
%if %{with python3}
Requires: %{name}-python3%{?_isa} = %{version}-%{release}
%endif
Requires: %{name}-random%{?_isa} = %{version}-%{release}
Requires: %{name}-regex%{?_isa} = %{version}-%{release}
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
Requires: %{name}-stacktrace%{?_isa} = %{version}-%{release}
Requires: %{name}-test%{?_isa} = %{version}-%{release}
Requires: %{name}-thread%{?_isa} = %{version}-%{release}
Requires: %{name}-timer%{?_isa} = %{version}-%{release}
Requires: %{name}-type_erasure%{?_isa} = %{version}-%{release}
Requires: %{name}-url%{?_isa} = %{version}-%{release}
Requires: %{name}-wave%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%if %{with python3}
Recommends: (boost-numpy3 if python3-numpy)
%endif
%if %{with python3}
%endif
%if %{with quadmath}
%endif
Patch0:        boost-1.81.0-build-optflags.patch
Patch1:        boost-1.90.0-no-rpath.patch
Patch2:        boost-1.73.0-cmakedir.patch
Patch3:        boost-1.78.0-b2-build-flags.patch
Patch5:        boost-1.76.0-fix-narrowing-conversions-for-ppc.patch
%bcond_with tests
%bcond_with docs_generated
# oreon:deps
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  libicu-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libzstd-devel
BuildRequires:  m4
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  which
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been included in the C++ 2011 standard and
others have been proposed to the C++ Standards Committee for inclusion
in future standards.)

%package atomic
Summary: Run-time component of boost atomic library
%description atomic

Run-time support for Boost.Atomic, a library that provides atomic data
types and operations on these data types, as well as memory ordering
constraints required for coordinating multiple threads through atomic
variables.

%package charconv
Summary: Run-time component of boost charconv library
License: BSL-1.0 AND (BSL-1.0 OR Apache-2.0 WITH LLVM-exception)
%description charconv

Run-time support for Boost.Charconv, an implementation of <charconv>
in C++11.

%package chrono
Summary: Run-time component of boost chrono library
License: BSL-1.0 AND (MIT OR NCSA)
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description chrono

Run-time support for Boost.Chrono, a set of useful time utilities.

%package cobalt
Summary: Run-time component of boost cobalt library
%description cobalt

Boost.Cobalt provides a set of easy to use coroutine primitives & utilities
running on top of boost.asio. These will be of interest for applications that
perform a lot of IO that want to not block unnecessarily, yet still want to
have linear & readable code (i..e. avoid callbacks).

%package container
Summary: Run-time component of boost container library
%description container

Boost.Container library implements several well-known containers,
including STL containers. The aim of the library is to offer advanced
features not present in standard containers or to offer the latest
standard draft features for compilers that don't comply with the
latest C++ standard.

%package contract
Summary: Run-time component of boost contract library
%description contract

Run-time support for boost contract library.
Contract programming for C++. All contract programming features are supported:
Subcontracting, class invariants, postconditions (with old and return values),
preconditions, customizable actions on assertion failure (e.g., terminate
or throw), optional compilation and checking of assertions, etc,
from Lorenzo Caminiti.

%if %{with context}
%package context
Summary: Run-time component of boost context switching library
%description context

Run-time support for Boost.Context, a foundational library that
provides a sort of cooperative multitasking on a single thread.

%package coroutine
Summary: Run-time component of boost coroutine library
Requires: %{name}-context%{?_isa} = %{version}-%{release}
%description coroutine
Run-time support for Boost.Coroutine, a library that provides
generalized subroutines which allow multiple entry points for
suspending and resuming execution.

%endif

%package date-time
Summary: Run-time component of boost date-time library
%description date-time

Run-time support for Boost Date Time, a set of date-time libraries based
on generic programming concepts.

%if %{with context}
%package fiber
Summary: Run-time component of boost fiber library
Requires: %{name}-context%{?_isa} = %{version}-%{release}
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
%description fiber

Run-time support for the Boost Fiber library, a framework for
micro-/userland-threads (fibers) scheduled cooperatively.
%endif

%package filesystem
Summary: Run-time component of boost filesystem library
Requires: %{name}-atomic%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description filesystem

Run-time support for the Boost Filesystem Library, which provides
portable facilities to query and manipulate paths, files, and
directories.

%package graph
Summary: Run-time component of boost graph library
License: BSL-1.0 AND (BSL-1.0 OR MIT)
Requires: %{name}-regex%{?_isa} = %{version}-%{release}
%description graph

Run-time support for the BGL graph library.  BGL interface and graph
components are generic, in the same sense as the Standard Template
Library (STL).

%package iostreams
Summary: Run-time component of boost iostreams library
%description iostreams

Run-time support for Boost.Iostreams, a framework for defining streams,
stream buffers and i/o filters.

%package json
Summary: Run-time component of boost json library
License: BSL-1.0 OR Apache-2.0
Requires: %{name}-container%{?_isa} = %{version}-%{release}
%description json

Run-time support for Boost.Json, a portable C++ library which provides
containers and algorithms that implement JavaScript Object Notation, or
simply "JSON"

%package locale
Summary: Run-time component of boost locale library
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Requires: %{name}-thread%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description locale

Run-time support for Boost.Locale, a set of localization and Unicode
handling tools.

%package log
Summary: Run-time component of boost logging library
Requires: %{name}-atomic%{?_isa} = %{version}-%{release}
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires: %{name}-regex%{?_isa} = %{version}-%{release}
Requires: %{name}-thread%{?_isa} = %{version}-%{release}
%description log

Run-time support for Boost.Log, a modular and extensible logging
library that supports both narrow-character and wide-character logging.

%package math
Summary: Run-time component of boost math toolkit
%description math

Run-time support for Boost.Math, including floating-point utilities,
specific width floating-point types, mathematical constants,
statistical distributions, special functions, and more.

%package nowide
Summary: Standard library functions with UTF-8 API on Windows
%description nowide

Run-time support for Boost.Nowide.

%if %{with python3}

%package numpy3
Summary: Run-time component of boost numpy library for Python 3
Requires: %{name}-python3%{?_isa} = %{version}-%{release}
Requires: python3-numpy
%description numpy3

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the NumPy extension of the Boost Python Library for Python 3.

%endif

%package process
Summary:  Run-time component of boost process library
%description process

Run-time support of the Boost.Process library, for managing system
processes.

%package program-options
Summary:  Run-time component of boost program_options library
%description program-options

Run-time support of boost program options library, which allows program
developers to obtain (name, value) pairs from the user, via
conventional methods such as command-line and configuration file.

%if %{with python3}
%package python3
Summary: Run-time component of boost python library for Python 3
Requires: python(abi)
%description python3

The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes,
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains run-time
support for the Boost Python Library compiled for Python 3.
%endif

%package random
Summary: Run-time component of boost random library
%description random

Run-time support for boost random library.

%package regex
Summary: Run-time component of boost regular expression library
%description regex

Run-time support for boost regular expression library.

%package serialization
Summary: Run-time component of boost serialization library
%description serialization

Run-time support for serialization for persistence and marshaling.

%package stacktrace
Summary: Run-time component of boost stacktrace library
%description stacktrace

Run-time component of the Boost stacktrace library.

%package test
Summary: Run-time component of boost test library
%description test

Run-time support for simple program testing, full unit testing, and for
program execution monitoring.

%package thread
Summary: Run-time component of boost thread library
License: BSL-1.0 AND (MIT OR NCSA)
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description thread

Run-time component Boost.Thread library, which provides classes and
functions for managing multiple threads of execution, and for
synchronizing data between the threads or providing separate copies of
data specific to individual threads.

%package timer
Summary: Run-time component of boost timer library
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description timer

"How long does my C++ code take to run?"
The Boost Timer library answers that question and does so portably,
with as little as one #include and one additional line of code.

%package type_erasure
Summary: Run-time component of boost type erasure library
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Requires: %{name}-thread%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description type_erasure

The Boost.TypeErasure library provides runtime polymorphism in C++
that is more flexible than that provided by the core language.

%package url
Summary: Runtime component of boost URL library
%description url

Run-time support for the Boost.URL library, a Standards conforming
library for parsing Uniform Resource Locators.

%package wave
Summary: Run-time component of boost C99/C++ preprocessing library
Requires: %{name}-chrono%{?_isa} = %{version}-%{release}
Requires: %{name}-date-time%{?_isa} = %{version}-%{release}
Requires: %{name}-filesystem%{?_isa} = %{version}-%{release}
Requires: %{name}-thread%{?_isa} = %{version}-%{release}
Obsoletes: boost-system < 1.90.0
Conflicts: boost-system < 1.90.0
%description wave

Run-time support for the Boost.Wave library, a Standards conforming,
and highly configurable implementation of the mandated C99/C++
preprocessor functionality.

%package devel
Summary: The Boost C++ headers and shared development libraries
License: BSL-1.0 AND MIT AND (MIT OR NCSA) AND (BSL-1.0 OR MIT) AND HPND-sell-variant AND Zlib AND Apache-2.0 AND (BSL-1.0 OR Apache-2.0) AND (BSL-1.0 OR Apache-2.0 WITH LLVM-exception)
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libicu-devel%{?_isa}
%if %{with quadmath}
Requires: libquadmath-devel%{?_isa}
%endif
%if %{with python3}
Requires: %{name}-numpy3%{?_isa} = %{version}-%{release}
Provides: %{name}-python3-devel = %{version}-%{release}
Provides: %{name}-python3-devel%{?_isa} = %{version}-%{release}
%endif
%description devel
Headers and shared object symbolic links for the Boost C++ libraries.

%package static
Summary: The Boost C++ static development libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static Boost C++ libraries.

%package doc
Summary: HTML documentation for the Boost C++ libraries
%if 0%{?rhel} >= 6 || (0%{?oreon} >= 11)
BuildArch: noarch
%endif
%description doc
This package contains the documentation in the HTML format of the Boost C++
libraries. The documentation provides the same content as that on the Boost
web page (http://www.boost.org/doc/libs/%{version_enc}).

%package examples
Summary: Source examples for the Boost C++ libraries
%if 0%{?rhel} >= 6 || (0%{?oreon} >= 11)
BuildArch: noarch
%endif
Requires: %{name}-devel = %{version}-%{release}
%description examples
This package contains example source files distributed with boost.

%if %{with openmpi}

%package openmpi
Summary: Run-time component of Boost.MPI library
BuildRequires: openmpi-devel
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
%description openmpi

Run-time support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-devel
Summary: Shared library symbolic links for Boost.MPI
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: %{name}-graph-openmpi%{?_isa} = %{version}-%{release}
%description openmpi-devel

Devel package for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%if %{with python3}

%package openmpi-python3
Summary: Python 3 run-time component of Boost.MPI library
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: %{name}-python3%{?_isa} = %{version}-%{release}
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
Requires: python3-openmpi%{?_isa}
%description openmpi-python3

Python 3 support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.

%package openmpi-python3-devel
Summary: Shared library symbolic links for Boost.MPI Python 3 component
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-openmpi-python3%{?_isa} = %{version}-%{release}
%description openmpi-python3-devel

Devel package for the Python 3 interface of Boost.MPI-OpenMPI, a library
providing a clean C++ API over the OpenMPI implementation of MPI.

%endif

%package graph-openmpi
Summary: Run-time component of parallel boost graph library
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
%description graph-openmpi

Run-time support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the Standard
Template Library (STL).  This libraries in this package use OpenMPI
back-end to do the parallel work.

%endif

%if %{with mpich}

%package mpich
Summary: Run-time component of Boost.MPI library
BuildRequires: mpich-devel
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
%description mpich

Run-time support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-devel
Summary: Shared library symbolic links for Boost.MPI
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: %{name}-graph-mpich%{?_isa} = %{version}-%{release}
%description mpich-devel

Devel package for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%if %{with python3}

%package mpich-python3
Summary: Python 3 run-time component of Boost.MPI library
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: %{name}-python3%{?_isa} = %{version}-%{release}
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
Requires: python3-mpich%{?_isa}
%description mpich-python3

Python 3 support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.

%package mpich-python3-devel
Summary: Shared library symbolic links for Boost.MPI Python 3 component
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-mpich-python3%{?_isa} = %{version}-%{release}
%description mpich-python3-devel

Devel package for the Python 3 interface of Boost.MPI-MPICH, a library
providing a clean C++ API over the MPICH implementation of MPI.

%endif

%package graph-mpich
Summary: Run-time component of parallel boost graph library
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: %{name}-serialization%{?_isa} = %{version}-%{release}
%description graph-mpich

Run-time support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the Standard
Template Library (STL).  This libraries in this package use MPICH
back-end to do the parallel work.

%endif

%package build
Summary: Cross platform build system for C++ projects
Requires: %{name}-b2
BuildArch: noarch
%description build
Boost.Build is an easy way to build C++ projects, everywhere. You name
your pieces of executable and libraries and list their sources.  Boost.Build
takes care about compiling your sources with the right options,
creating static and shared libraries, making pieces of executable, and other
chores -- whether you are using GCC, MSVC, or a dozen more supported
C++ compilers -- on Windows, OSX, Linux and commercial UNIX systems.

%package doctools
Summary: Tools for working with Boost documentation
Requires: docbook-dtds
Requires: docbook-style-xsl
%description doctools

Tools for working with Boost documentation in BoostBook or QuickBook format.

%package b2
Summary: A low-level build tool
%description b2
B2 (formerly Boost.Jam) is the low-level build engine tool for Boost.Build.
Historically, B2 was based on on FTJam and on Perforce Jam but has grown
a number of significant features and is now developed independently.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{toplev_dirname} -p1
find ./boost -name '*.hpp' -perm /111 | xargs --no-run-if-empty chmod a-x

%build

%set_build_flags
%if %{with python3}
PYTHON3_ABIFLAGS=$(/usr/bin/python3-config --abiflags)
: PYTHON3_VERSION=%{python3_version}
: PYTHON3_ABIFLAGS=${PYTHON3_ABIFLAGS}
%endif
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-unused-local-typedefs -Wno-deprecated-declarations"
export RPM_LD_FLAGS
cat > ./tools/build/src/user-config.jam << "EOF"
import os ;
local RPM_OPT_FLAGS = [ os.environ RPM_OPT_FLAGS ] ;
local RPM_LD_FLAGS = [ os.environ RPM_LD_FLAGS ] ;
using %{toolchain} : : : <compileflags>$(RPM_OPT_FLAGS) <linkflags>$(RPM_LD_FLAGS) ;
%if %{with openmpi} || %{with mpich}
using mpi ;
%endif
EOF
%if %{with python3}
cat >> ./tools/build/src/user-config.jam << EOF
using python : %{python3_version} : /usr/bin/python3 : /usr/include/python%{python3_version}${PYTHON3_ABIFLAGS} : : : ;
EOF
%endif
./bootstrap.sh --with-toolset=%{toolchain} --with-icu --prefix=$RPM_BUILD_ROOT%{_prefix}
echo ============================= build serial ==================
./b2 -q %{?_smp_mflags} \
	--without-mpi --without-graph_parallel --build-dir=serial \
%if !%{with context}
	--without-context --without-coroutine \
	--without-fiber \
%endif
	variant=release threading=multi debug-symbols=on pch=off \
%if %{with python3}
	python=%{python3_version} \
%endif
%if !%{with stacktrace_from_exception}
	boost.stacktrace.from_exception=off \
%endif
	stage
%if %{with openmpi} || %{with mpich}
module purge ||:
%endif
%if %{with openmpi}
%{_openmpi_load}
%if %{with python3}
echo ============================= build $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} \
	--with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER \
	variant=release threading=multi debug-symbols=on pch=off \
	python=%{python3_version} stage
%endif
%{_openmpi_unload}
export PATH=/bin${PATH:+:}$PATH
%endif
%if %{with mpich}
%{_mpich_load}
%if %{with python3}
echo ============================= build $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} \
	--with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER \
	variant=release threading=multi debug-symbols=on pch=off \
	python=%{python3_version} stage
%endif
%{_mpich_unload}
export PATH=/bin${PATH:+:}$PATH
%endif
echo ============================= build Boost.Build ==================
(cd tools/build
 ./bootstrap.sh --with-toolset=%{toolchain} --prefix=$RPM_BUILD_ROOT%{_prefix})
%check

:
%install
cd %{_builddir}/%{toplev_dirname}
%if %{with openmpi} || %{with mpich}
module purge ||:
%endif
%if %{with openmpi}
%{_openmpi_load}
%if %{with python3}
echo ============================= install $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} \
	--with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER \
	--stagedir=${RPM_BUILD_ROOT}${MPI_HOME} \
	variant=release threading=multi debug-symbols=on pch=off \
	python=%{python3_version} stage
mkdir -p ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost
touch ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/boost-python%{python3_version}/mpi.so \
   ${RPM_BUILD_ROOT}%{python3_sitearch}/openmpi/boost/
%endif
sed -i -e 's|get_filename_component(_BOOST_INCLUDEDIR "${_BOOST_CMAKEDIR}/.*"|get_filename_component(_BOOST_INCLUDEDIR "${_BOOST_CMAKEDIR}/../../../../include"|' ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/*/*-config.cmake
rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_{python,{w,}serialization}*
rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_numpy*
rm -rf ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/boost_{python,{w,}serialization}*
rm -rf ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/boost_numpy*
%{_openmpi_unload}
export PATH=/bin${PATH:+:}$PATH
%endif
%if %{with mpich}
%{_mpich_load}
%if %{with python3}
echo ============================= install $MPI_COMPILER ==================
./b2 -q %{?_smp_mflags} \
	--with-mpi --with-graph_parallel --build-dir=$MPI_COMPILER \
	--stagedir=${RPM_BUILD_ROOT}${MPI_HOME} \
	variant=release threading=multi debug-symbols=on pch=off \
	python=%{python3_version} stage
mkdir -p ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost
touch ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost/__init__.py
mv ${RPM_BUILD_ROOT}${MPI_HOME}/lib/boost-python%{python3_version}/mpi.so \
   ${RPM_BUILD_ROOT}%{python3_sitearch}/mpich/boost/
%endif
sed -i -e 's|get_filename_component(_BOOST_INCLUDEDIR "${_BOOST_CMAKEDIR}/.*"|get_filename_component(_BOOST_INCLUDEDIR "${_BOOST_CMAKEDIR}/../../../../include"|' ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/*/*-config.cmake
rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_{python,{w,}serialization}*
rm -f ${RPM_BUILD_ROOT}${MPI_HOME}/lib/libboost_numpy*
rm -rf ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/boost_{python,{w,}serialization}*
rm -rf ${RPM_BUILD_ROOT}${MPI_HOME}/lib/cmake/boost_numpy*
%{_mpich_unload}
export PATH=/bin${PATH:+:}$PATH
%endif
echo ============================= install serial ==================
./b2 -q %{?_smp_mflags} \
	--without-mpi --without-graph_parallel --build-dir=serial \
%if !%{with context}
	--without-context --without-coroutine \
	--without-fiber \
%endif
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--libdir=$RPM_BUILD_ROOT%{_libdir} \
	variant=release threading=multi debug-symbols=on pch=off \
%if %{with python3}
	python=%{python3_version} \
%endif
%if !%{with stacktrace_from_exception}
	boost.stacktrace.from_exception=off \
%endif
	install
cat > $RPM_BUILD_ROOT%{_libdir}/libboost_system.so << EOT
/* GNU ld script
There is no runtime library for Boost.System.
This empty linker script exists to support Fedora packages which use
-lboost_system when linking and so require a library with that name.
This linker script will be remove in a future Fedora release.
*/
EOT
chmod 644 $RPM_BUILD_ROOT%{_libdir}/libboost_system.so
echo ============================= install Boost.Build ==================
(cd tools/build
 ./b2 --prefix=$RPM_BUILD_ROOT%{_prefix} install
 mv $RPM_BUILD_ROOT%{_datadir}/b2 $RPM_BUILD_ROOT%{_datadir}/boost-build
 pushd $RPM_BUILD_ROOT%{_datadir}/
 ln -s ./boost-build b2
 popd
 chmod +x $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxproc.py
 sed -i '1s@^#!/usr/bin.python$@&3@' $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxproc.py
 rm $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxygen/windows-paths-check.hpp
 rm -f $RPM_BUILD_ROOT%{_datadir}/boost-build/src/tools/doxygen/windows-paths-check.hpp
 %{__install} -p -m 644 %{SOURCE1} -D $RPM_BUILD_ROOT%{_mandir}/man1/b2.1
)
echo ============================= install Boost.QuickBook ==================
(cd tools/quickbook
 ../build/b2 --prefix=$RPM_BUILD_ROOT%{_prefix}
 %{__install} -p -m 755 ../../dist/bin/quickbook $RPM_BUILD_ROOT%{_bindir}/
 cd ../boostbook
 find dtd -type f -name '*.dtd' | while read tobeinstalledfiles; do
   install -p -m 644 $tobeinstalledfiles -D $RPM_BUILD_ROOT%{_datadir}/boostbook/$tobeinstalledfiles
 done
 find xsl -type f | while read tobeinstalledfiles; do
   install -p -m 644 $tobeinstalledfiles -D $RPM_BUILD_ROOT%{_datadir}/boostbook/$tobeinstalledfiles
 done
)
echo ============================= install documentation ==================
rm -rf %{boost_docdir} && %{__mkdir_p} %{boost_docdir}/html
DOCPATH=%{boost_docdir}
DOCREGEX='.*\.\(html?\|css\|png\|gif\)'
find libs doc more -type f -regex $DOCREGEX \
    | sed -n '/\//{s,/[^/]*$,,;p}' \
    | sort -u > tmp-doc-directories
sed "s:^:$DOCPATH/:" tmp-doc-directories \
    | xargs -P 0 --no-run-if-empty %{__install} -d
cat tmp-doc-directories | while read tobeinstalleddocdir; do
    find $tobeinstalleddocdir -mindepth 1 -maxdepth 1 -regex $DOCREGEX -print0 \
    | xargs -P 0 -0 %{__install} -p -m 644 -t $DOCPATH/$tobeinstalleddocdir
done
rm -f tmp-doc-directories
%{__install} -p -m 644 -t $DOCPATH LICENSE_1_0.txt index.htm index.html boost.png rst.css boost.css
echo ============================= install examples ==================
sed -i -e 's/\r//g' libs/geometry/example/ml02_distance_strategy.cpp
for tmp_doc_file in flyweight/example/Jamfile.v2 \
 format/example/sample_new_features.cpp multi_index/example/Jamfile.v2 \
 multi_index/example/hashed.cpp serialization/example/demo_output.txt
do
  mv libs/${tmp_doc_file} libs/${tmp_doc_file}.iso8859
  iconv -f ISO8859-1 -t UTF8 < libs/${tmp_doc_file}.iso8859 > libs/${tmp_doc_file}
  touch -r libs/${tmp_doc_file}.iso8859 libs/${tmp_doc_file}
  rm -f libs/${tmp_doc_file}.iso8859
done
rm -rf %{boost_examplesdir} && mkdir -p %{boost_examplesdir}/html
EXAMPLESPATH=%{boost_examplesdir}
find libs -type d -name example -exec find {} -type f \; \
    | sed -n '/\//{s,/[^/]*$,,;p}' \
    | sort -u > tmp-doc-directories
sed "s:^:$EXAMPLESPATH/:" tmp-doc-directories \
    | xargs -P 0 --no-run-if-empty %{__install} -d
rm -f tmp-doc-files-to-be-installed && touch tmp-doc-files-to-be-installed
cat tmp-doc-directories | while read tobeinstalleddocdir
do
  find $tobeinstalleddocdir -mindepth 1 -maxdepth 1 -type f \
    >> tmp-doc-files-to-be-installed
done
cat tmp-doc-files-to-be-installed | while read tobeinstalledfiles
do
  if test -s $tobeinstalledfiles
  then
    tobeinstalleddocdir=`dirname $tobeinstalledfiles`
    %{__install} -p -m 644 -t $EXAMPLESPATH/$tobeinstalleddocdir $tobeinstalledfiles
  fi
done
rm -f tmp-doc-files-to-be-installed
rm -f tmp-doc-directories
%{__install} -p -m 644 -t $EXAMPLESPATH LICENSE_1_0.txt
(cd $RPM_BUILD_ROOT/%{_datadir}
 rm boost_predef/tools/check/*
 rm boost_predef/build.jam
)
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post doctools

CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://www.boost.org/tools/boostbook/dtd" \
 "file://%{_datadir}/boostbook/dtd" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://www.boost.org/tools/boostbook/dtd" \
 "file://%{_datadir}/boostbook/dtd" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://www.boost.org/tools/boostbook/xsl" \
 "file://%{_datadir}/boostbook/xsl" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://www.boost.org/tools/boostbook/xsl" \
 "file://%{_datadir}/boostbook/xsl" $CATALOG
%postun doctools

if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
    "file://%{_datadir}/boostbook/dtd" $CATALOG
  %{_bindir}/xmlcatalog --noout --del \
    "file://%{_datadir}/boostbook/xsl" $CATALOG
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
