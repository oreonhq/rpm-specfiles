# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 12833fd234ad679b8bd42b28c07c9141b9f788b3b11ebedec33d2e6c3cb02c9c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: babeltrace2
Version: 2.1.2
Release: 1%{?dist}
Summary: A trace manipulation toolkit
License: MIT AND GPL-2.0-only
URL: https://www.efficios.com/babeltrace
Source0: https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2
Source1: https://www.efficios.com/files/babeltrace/babeltrace2-%{version}.tar.bz2.asc
Source2: gpgkey-7F49314A26E0DE78427680E05F1B2A0789F12B11.gpg
Patch0: 0001-Fix-bt2.TraceCollectionMessageIterator-avoid-circula.patch
Patch1: babeltrace2-swig45.patch

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf >= 2.69
BuildRequires: automake >= 1.13
BuildRequires: bison >= 2.5
BuildRequires: elfutils-devel >= 0.154
BuildRequires: flex >= 2.5.35
BuildRequires: clang
BuildRequires: glib2-devel >= 2.28.0
BuildRequires: gnupg2
BuildRequires: libtool >= 2.2
BuildRequires: make
BuildRequires: python3-devel >= 3.4
BuildRequires: python3-setuptools
BuildRequires: swig >= 3.0

Requires: libbabeltrace2%{?_isa} = %{version}-%{release}

%description
The Babeltrace 2 project offers a library with a C API, Python 3 bindings, and
a command-line tool which makes it very easy for mere mortals to view,
convert, transform, and analyze traces.

Babeltrace 2 is also the reference parser implementation of the Common Trace
Format (CTF), a very versatile trace format followed by various tracers and
tools such as LTTng and barectf.

%package -n libbabeltrace2
Summary: A trace manipulation library

%description -n libbabeltrace2
The libbabeltrace2 package contains a library and plugin system to view,
convert, transform, and analyze traces.

%package -n libbabeltrace2-devel
Summary: Development files for libbabeltrace2
Requires: libbabeltrace2%{?_isa} = %{version}-%{release}
Requires: glib2-devel

%description -n libbabeltrace2-devel
The libbabeltrace2-devel package contains the header files and libraries
needed to develop programs that use the libbabeltrace2 trace manipulation
library.

%package -n python3-bt2
Summary: libbabeltrace2 Python bindings
Requires: libbabeltrace2%{?_isa} = %{version}-%{release}

%description -n python3-bt2
The python3-bt2 package provides Python 3 bindings for libbabeltrace2.

%prep
%oreon_sha256
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
autoreconf -vif
export PYTHON=%{__python3}
export PYTHON_CONFIG=%{__python3}-config
%configure --disable-static \
    --enable-python-bindings \
    --enable-python-plugins \
    --enable-debug-info \
    --disable-Werror
%make_build V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}%{_pkgdocdir}/CONTRIBUTING.adoc
rm -f %{buildroot}%{_pkgdocdir}/LICENSE
rm -f %{buildroot}%{_pkgdocdir}/std-ext-lib.md

%check
%make_build check

%files
%doc ChangeLog
%doc README.adoc
%license LICENSE
%{_bindir}/babeltrace2
%{_mandir}/man1/*.1*
%{_mandir}/man7/*.7*

%files -n libbabeltrace2
%license LICENSE
%{_libdir}/libbabeltrace2.so.*
%{_libdir}/libbabeltrace2-ctf-writer.so.*
%{_libdir}/babeltrace2/plugin-providers/*.so
%{_libdir}/babeltrace2/plugins/*.so

%files -n libbabeltrace2-devel
%{_includedir}/babeltrace2/
%{_includedir}/babeltrace2-ctf-writer/
%{_libdir}/libbabeltrace2.so
%{_libdir}/libbabeltrace2-ctf-writer.so
%{_libdir}/pkgconfig/babeltrace2.pc
%{_libdir}/pkgconfig/babeltrace2-ctf-writer.pc

%files -n python3-bt2
%{python3_sitearch}/bt2
%{python3_sitearch}/bt2*.egg-info

%changelog
%autochangelog
