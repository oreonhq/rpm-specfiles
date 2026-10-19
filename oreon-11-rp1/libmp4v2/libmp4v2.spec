%global source0_hash d8dac40ba702350dd4ce15626285a5b4b6086b212ec9e6b2e8a1651ace78234d
%global svnversion 507
%global gver .trunkREV%{svnversion}
Summary:        Library for working with files using the mp4 container format
Name: libmp4v2
Version: 2.1.0
Release:        1%{?dist}
License: LicenseRef-Callaway-MPLv1.1
URL: http://code.google.com/p/mp4v2
Source0:        http://mp4v2.googlecode.com/files/mp4v2-trunk-r%{svnversion}.tar.bz2
Source1: make-svn-snapshot.sh
Patch1: 0001-Fix-make-dist.patch
Patch2: 0002-Install-man-man3-BTW-like-in-libmp4v2-1.5.0.1.patch
Patch3: 0003-Fix-out-of-tree-builds-182.patch
Patch4: 0004-Fix-GCC7-build.patch
Patch5: 0005-Fix-clang-compilation.patch
Patch7: 0007-Fix-Out-of-bounds-memory-access-in-MP4v2-2.0.0.patch
Patch8: 0008-Fix-v2-Type-confusion-in-MP4v2-2.0.0.patch
Patch9: 0009-Null-out-pointer-after-free-to-prevent-double-free.patch
Patch10: 0010-Fix-v3-Integer-underflow-overflow-in-MP4v2-2.0.0.patch
Patch50: gcc10.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  svn
BuildRequires:  texinfo
# /oreon:deps
%description
The libmp4v2 library provides an abstraction layer for working with files
using the mp4 container format. This library is developed by mpeg4ip project
and is an exact copy of the library distributed in the mpeg4ip package.

%package devel
Summary: Development files for the mp4v2 library
Requires: %{name}%{_isa} = %{version}-%{release}
%description devel
Development files and documentation needed to develop and compile programs
using the libmp4v2 library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir mp4v2-trunk
%oreon_prep
%build

autoreconf --force --install --verbose
%configure --disable-static
%make_build
export LANG=en_US.utf8
%{__make} api
%install
%make_install
find %{buildroot} -name '*.la' -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmp4v2-devel -f %{oreon_filedir}/libmp4v2-devel.list

%changelog

%autochangelog
