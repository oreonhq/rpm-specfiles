%global source0_hash 25e194b92d8e1c1bba0127f514c5fcabc7a14df47ac7ed7aec33f1839d138cf5
Name:           NearTree
Version:        5.1.1
Release:        15%{?dist}
Summary:        An API for finding nearest neighbors
License:        LGPLv2+
URL:            http://neartree.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/neartree/neartree/NearTree-%{version}/NearTree-%{version}.tar.gz
Patch0:         NearTree-5.1.1-fedora.patch
Patch1:         NearTree-5.1.1-lib64.patch
# oreon:deps
BuildRequires:  CVector-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  time
# /oreon:deps
%description
This is a release of an API for finding nearest neighbors among
points in spaces of arbitrary dimensions. This release provides a
C++ template, TNear.h, and a C library, CNearTree.c, with
example/test programs.

%package devel
Summary:        Development tools for compiling programs using NearTree
Requires:       %{name} = %{version}-%{release}
Requires:       CVector-devel
%description devel
The NearTree-devel package includes the header and library files for
developing applications that use NearTree.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fedora
%if 0%{?__isa_bits} == 64
%patch -P1 -p1 -b .lib64
%endif

# convert end of line code from CRFL to LF
mv README_NearTree.txt README_NearTree.txt.orig
tr -d \\r < README_NearTree.txt.orig > README_NearTree.txt

%build

make all CFLAGS="%{optflags} -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1" %{?_smp_mflags}
%install
make install CFLAGS="%{optflags} -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1" INSTALL_PREFIX="%{buildroot}%{_prefix}"
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
%oreon_autofiles NearTree-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifnarch ( %{ix86} && %{s390x} )
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n NearTree-devel -f %{oreon_filedir}/NearTree-devel.list

%changelog

%autochangelog
