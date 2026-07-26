%global source0_hash b951eb23bb4235ada82cef85b9f129bf74a14e45d992097431e7bfb6bdca6642

Name:           NearTree
Version:        5.1.1
Release:        15%{?dist}
Summary:        An API for finding nearest neighbors

License:        LGPLv2+
URL:            http://neartree.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/neartree/neartree/NearTree-%{version}/NearTree-%{version}.tar.gz
# library should not have version number in their name.
# Sent to upstream but upstream cannot accept.
Patch0:         NearTree-5.1.1-fedora.patch
# to fix libdir for lib64 architecture
Patch1:         NearTree-5.1.1-lib64.patch
BuildRequires: make
BuildRequires:  libtool time CVector-devel
BuildRequires:  gcc-c++

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

# remove .la and .a files
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%check
# Fails on i686 for some reason
%ifnarch ( %{ix86} && %{s390x} )
# make tests CFLAGS="%{optflags} -fno-caller-saves -ansi -pedantic -DCNEARTREE_SAFE_TRIANG=1"
%endif

%ldconfig_scriptlets

%files
%doc README_NearTree.html README_NearTree.txt lgpl.txt
%{_libdir}/libCNearTree.so.*

%files devel
%{_includedir}/CNearTree.h
%{_includedir}/TNear.h
%{_includedir}/rhrand.h
%{_includedir}/triple.h
%{_libdir}/libCNearTree.so

%changelog
%autochangelog
