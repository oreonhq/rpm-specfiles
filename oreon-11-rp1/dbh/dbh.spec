%global source0_hash 8df54e7d1c1d071e385b59256b42a9538cb1b744b11ecc022e188d99046e91d7

%undefine _hardened_build
%global debug_package %{nil}
Summary: Disk based hash library
Name: dbh
Version: 5.0.22
Release: 3%{?dist}
URL: http://dbh.sourceforge.net/
Source0: http://downloads.sourceforge.net/%{name}/lib%{name}2-%{version}.tar.gz
Patch0: %{name}-5.0.13-bigendian.patch
Epoch: 1
License: GPL-3.0-or-later
BuildRequires:  gcc
BuildRequires: glib2-devel
BuildRequires: make

%description 
Disk based hashes is a method to create multidimensional binary trees on disk.
This library permits the extension of database concept to a plethora of 
electronic data, such as graphic information. With the multidimensional binary 
tree it is possible to mathematically prove that access time to any 
particular record is minimized (using the concept of critical points from 
calculus), which provides the means to construct optimized databases for 
particular applications.

%package devel
Summary: Header files for disk based hash library
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
This package includes the static libraries and header files you will need
to compile applications for dbh.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn lib%{name}2-%{version}
%patch -P0 -p1 -b .bigendian

%build
./autogen.sh
%configure --disable-static

%make_build

%install
%make_install

mv $RPM_BUILD_ROOT/usr/share/gtk-doc .
rm -rf $RPM_BUILD_ROOT/usr/share/dbh

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.2*

%files devel
%doc examples/*.c examples/Makefile* doc/html gtk-doc
%{_libdir}/lib*.so
%{_datadir}/pkgconfig/*
%{_includedir}/*
#%%{_mandir}/man1/dbh*
%{_mandir}/man3/dbh*

%changelog
%autochangelog
