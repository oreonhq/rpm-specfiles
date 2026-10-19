%global source0_hash 381c8f52a9df09ff75f23955927c3fd6ae7d522e979c4898b1d9e8c45c1e06db
Name: fmt-ptrn
Version: 1.3.24
Release:        1%{?dist}
License: GPL-2.0-or-later
Source0:        http://www.flyn.org/projects/%{name}/%{name}-%{version}.tar.gz
URL: http://www.flyn.org
Summary:        A simple template system
Requires: zlib
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description 
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file.

For example, given the following template:

//   FILE: %%(FILE)
// AUTHOR: %%(FULLNAME)
//   DATE: %%(DATE)

// Copyright (C) 1999 %%(FULLNAME) %%(EMAIL)
// All rights reserved.

nf will create:

//   FILE: foo.cpp
// AUTHOR: W. Michael Petullo
//   DATE: 11 September 1999

// Copyright (C) 1999 W. Michael Petullo new@flyn.org
// All rights reserved.
on my computer.

The program understands plaintext or gziped template files.

The fmt-ptrn system also provides a shared library which allows a 
programmer access to nf's functionality. The system was developed to 
be light and fast. Its only external dependencies are the C library, 
glib2 and zlib.

%post

/sbin/ldconfig
%postun

/sbin/ldconfig
%package devel
Summary: Files needed to develop applications using fmt-ptrn's libraries
Requires: fmt-ptrn = %{version}-%{release}, glib2-devel, zlib-devel
%description devel
New is a template system, especially useful in conjunction with a 
simple text editor such as vi. The user maintains templates which 
may contain format strings. At run time, nf replaces the format 
strings in a template with appropriate values to create a new file. 
This package provides the libraries, include files, and other 
resources needed for developing applications using fmt-ptrn's API.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

 %configure  --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewfmt-ptrn.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libnewtemplate.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fmt-ptrn-devel -f %{oreon_filedir}/fmt-ptrn-devel.list

%changelog

%autochangelog
