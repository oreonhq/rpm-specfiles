# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6984c9bd754be2fbcf896a0a8bd5b659cd231935a3cce7b8554bfc25ceac91e7

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           newt
Version:        0.52.25
Release:        1%{?dist}
Summary:        A library for text mode user interfaces
License:        LGPL-2.0-only
URL:            https://pagure.io/newt
Source0:        https://github.com/mlichvar/newt/archive/r0-52-25/newt-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  autoconf
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
%bcond_with lynx_docs
%if %{with lynx_docs}
BuildRequires:  lynx
%endif
BuildRequires:  make
BuildRequires:  popt-devel
BuildRequires:  python3-devel
BuildRequires:  slang-devel

%description
Newt is a programming library for color text mode, widget based user
interfaces. Newt can be used to add stacked windows, entry widgets,
checkboxes, radio buttons, labels, plain text fields, scrollbars,
etc., to text mode user interfaces. This package also contains the
shared library needed by programs built with newt, as well as a
/usr/bin/dialog replacement called whiptail. Newt is based on the
slang library.

%package devel
Summary:        Newt windowing toolkit development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       slang-devel

%description devel
The newt-devel package contains the header files and libraries
necessary for developing applications which use newt. Newt is a
development library for text mode user interfaces. Newt is based on
the slang library.

Install newt-devel if you want to develop applications which will use
newt.

%package -n python3-newt
Summary:        Python 3 bindings for newt
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-python3 = %{version}-%{release}
Provides:       %{name}-python3%{?_isa} = %{version}-%{release}
Provides:       snack = %{version}-%{release}

%description -n python3-newt
The python3-newt package contains the Python 3 bindings for the newt library
providing a python API for creating text mode interfaces.

%prep
%oreon_sha256
%autosetup -n newt-r0-52-25
./autogen.sh

%build
%configure --without-tcl
%make_build all
chmod 0644 peanuts.py popcorn.py
docbook2txt tutorial.sgml

%install
%make_install
rm -f %{buildroot}%{_libdir}/libnewt.a
%find_lang %{name}

%check
%make_build check

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGES README
%{_bindir}/whiptail
%{_libdir}/libnewt.so.*
%{_mandir}/man1/whiptail.1*

%files devel
%doc tutorial.*
%{_includedir}/newt.h
%{_libdir}/libnewt.so
%{_libdir}/pkgconfig/libnewt.pc

%files -n python3-newt
%doc peanuts.py popcorn.py
%{python3_sitearch}/*.so
%{python3_sitearch}/*.py*
%{python3_sitearch}/__pycache__/*.py*

%changelog
%autochangelog
