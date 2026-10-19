%global source0_hash 8b642127880e92e8a75400125307724635ecdf4020ca4481e5efe7640451bb92
%global somajor 1
%global sominor 10
%global soupd 1
%global optflags %optflags -std=gnu17
Name:		libxsmm
Version:	2.1.0
Release:        1%{?dist}
Summary:        Small dense or sparse matrix multiplications and convolutions for x86_64
License:	BSD-3-Clause
URL:		https://github.com/hfp/libxsmm
Source0:        https://github.com/hfp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		libxsmm-rpath.patch
ExclusiveArch:	x86_64
%global __requires_exclude /bin/.*sh$
%{?filter_setup:
%filter_from_requires /\/bin\/.*sh$/d
%filter_setup
}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  openblas-devel
BuildRequires:  python3-devel
# /oreon:deps
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

%global makeflags STATIC=0 SYM=1 AVX=0 PYTHON=%python3 PREFIX=%_prefix POUTDIR=%_lib PPKGDIR=%_lib/pkgconfig VERSION_API=1 OMPLIB=-lgomp
%make_build %makeflags
%install
%make_install %makeflags
mkdir -p %buildroot%_fmoddir %buildroot%_libdir/pkgconfig
mv %buildroot%_includedir/libxsmm.mod %buildroot%_fmoddir
rm -r %buildroot%_datadir/libxsmm
find samples -name .make | xargs rm
cp Makefile.inc samples		# included by the sub-directories
echo "These are set up to be built in the original source tree.
You will have to adjust the make files to use an installed version." >samples/README
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

OMP_NUM_THREADS=1 make test-cp2k %makeflags
rm -r samples/cp2k/{.make,.state,cp2k-dbcsr,cp2k-collocate,cp2k-test.txt}
rm -rf samples/cp2k/obj
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libxsmm-devel -f %{oreon_filedir}/libxsmm-devel.list
%files -n libxsmm-doc -f %{oreon_filedir}/libxsmm-doc.list

%changelog

%autochangelog
