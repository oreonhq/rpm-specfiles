# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f557911bf6171621e1f72ff35f5b1825bb35b52ed45325dcdee931e5d3c0787a
%global source2_hash 76fbde2d996f9e38d8f33abf6409b448ae556ad0f226ba7155b103eb7365c19e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary:          Library to support IDNA2008 internationalized domain names
Name:             libidn2
Version:        2.3.8
Release:        1%{?dist}
License:          (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:              https://www.gnu.org/software/libidn/#libidn2

Source0:        https://mirror.cs.odu.edu/gnu/libidn/libidn2-%{version}.tar.gz
Source1:        libidn2-2.3.8.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/B1D2BD1375BECB784CF4F8C4D73CF638C53C06BE

BuildRequires:    gnupg2
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    gettext
BuildRequires:    libunistring-devel
BuildRequires:    texinfo
BuildRequires:  oreon-rpm-macros
Provides:         bundled(gnulib)

%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package devel
Summary:          Development files for libidn2
Requires:         %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description devel
The libidn2-devel package contains libraries and header files for
developing applications that use libidn2.

%package -n idn2
Summary:          IDNA2008 internationalized domain names conversion tool
License:          GPL-3.0-or-later
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description -n idn2
The idn2 package contains the idn2 command line tool for testing
IDNA2008 conversions.

%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%setup -q

%build
%configure --disable-static
%make_build
%make_build -C doc html

%install
%make_install

# Clean-up examples for documentation
%make_build -C examples distclean
rm -f examples/Makefile*

# Don't install any libtool .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_datadir}/info/dir

%find_lang %{name}

%check
%make_build -C tests check

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%doc AUTHORS NEWS README.md
%{_libdir}/%{name}.so.0*

%files devel
%doc doc/%{name}.html examples
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/idn2.h
%{_mandir}/man3/idn2_*.3*
%{_datadir}/gtk-doc/

%files -n idn2
%{_bindir}/idn2
%{_mandir}/man1/idn2.1*
%{_infodir}/%{name}.info*

