%global source0_hash 9083fcacc4d85f2b8c3a3254112129c02d940d20db8c0c5bcb6239b115e8d0e8

%define __cmake_in_source_build 1
%global __soversion 2.0

Name:		biblesync
Version:	2.1.0
Release:	17%{?dist}
Summary:	A Cross-platform library for sharing Bible navigation

License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.xiphos.org
Source0:	https://github.com/karlkleinpaste/biblesync/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:		4b00f9fd3d0c858947eee18206ef44f9f6bd2283.patch

BuildRequires:	intltool
BuildRequires:	libuuid-devel
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires: make

%description
BibleSync is a multicast protocol to support Bible software shared co-
navigation. It uses LAN multicast in either a personal/small team mutual
navigation motif or in a classroom environment where there are Speakers plus
the Audience. It provides a complete yet minimal public interface to support
mode setting, setup for packet reception, transmit on local navigation, and
handling of incoming packets.

This library is not specific to any particular Bible software framework,
completely agnostic as to structure of layers above BibleSync.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libuuid-devel%{?_isa}

%description devel
This package contains libraries and header files for developing applications
that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIC"
mkdir build
pushd build
%cmake -DLIBDIR=%{_libdir} .. -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" -DBIBLESYNC_SOVERSION=%{__soversion}
%cmake_build
popd

%install
pushd build
%cmake_install
popd

%files
%doc LICENSE
%{_libdir}/libbiblesync.so.%{__soversion}

%files devel
%doc AUTHORS COPYING ChangeLog README.md WIRESHARK
%{_includedir}/biblesync
%{_libdir}/pkgconfig/biblesync.pc
%{_libdir}/libbiblesync.so
%{_mandir}/man7/biblesync.7*

%changelog
%autochangelog
