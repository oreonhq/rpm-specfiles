%global source0_hash 6ac9f76c2af010f97e916e4bae1cece341dc64ca28e3881ff4ddc3bc334060d7

# Copyright (c) 2008, 2009 David Sugar, Tycho Softworks.
# This file is free software; as a special exception the author gives
# unlimited permission to copy and/or distribute it, with or without
# modifications, as long as this notice is preserved.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.

Name:          ucommon
Version:       7.0.0
Release:       27%{?dist}
Summary:       Portable C++ framework for threads and sockets

License:       LGPL-3.0-or-later
URL:           http://www.gnu.org/software/commoncpp
Source0:       https://ftpmirror.gnu.org/commoncpp/ucommon-%{version}.tar.gz
# Raise minimum cmake version to 3.5
Patch0:        ucommon_cmakever.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: graphviz-gd
BuildRequires: gnutls-devel

%description
GNU uCommon C++ is a lightweight library to facilitate using C++ design
patterns even for very deeply embedded applications, such as for systems using
uclibc along with POSIX threading support. For this reason, uCommon disables
language features that consume memory or introduce runtime overhead. UCommon
introduces some design patterns from Objective-C, such as reference counted
objects, memory pools, and smart pointers. UCommon introduces some new concepts
for handling of thread locking and synchronization.  Starting with release
5.0, GNU uCommon also bundles GNU Common C++ libraries.

%package bin
Summary:       GNU uCommon system and support applications
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description bin
This is a collection of command line tools that use various aspects of the
ucommon library. Some may be needed to prepare files or for development of
applications.

%package devel
Summary:       Headers for building GNU uCommon applications
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      openssl-devel%{?_isa}
Requires:      pkgconfig

%description devel
This package provides header and support files needed for building
applications that use the uCommon and commoncpp libraries.

%package doc
Summary: Generated class documentation for GNU uCommon

%description doc
Generated class documentation for GNU uCommon library from header files in
HTML format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
export CXXFLAGS="-std=c++14 %{optflags}"
%cmake -DBUILD_DOCS=ON
%cmake_build
%cmake_build --target doc

%install
%cmake_install

%files
%doc AUTHORS README NEWS SUPPORT ChangeLog
%license COPYING COPYING.LESSER
%{_libdir}/libucommon.so.8*
%{_libdir}/libusecure.so.8*
%{_libdir}/libcommoncpp.so.8*

%files bin
%{_bindir}/args
%{_bindir}/mdsum
%{_bindir}/pdetach
%{_bindir}/sockaddr
%{_bindir}/zerofill
%{_bindir}/scrub-files
%{_bindir}/car
%{_bindir}/keywait
%{_bindir}/urlout
%{_mandir}/man1/args.*
%{_mandir}/man1/car.*
%{_mandir}/man1/mdsum.*
%{_mandir}/man1/pdetach.*
%{_mandir}/man1/scrub-files.*
%{_mandir}/man1/sockaddr.*
%{_mandir}/man1/zerofill.*
%{_mandir}/man1/keywait.*
%{_mandir}/man1/urlout.*

%files devel
%{_bindir}/ucommon-config
%{_bindir}/commoncpp-config
%{_datadir}/%{name}/
%{_includedir}/ucommon/
%{_includedir}/commoncpp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/ucommon-config.*
%{_mandir}/man1/commoncpp-config.*

%files doc
%doc %{_vpath_builddir}/doc/html/*

%changelog
%autochangelog
