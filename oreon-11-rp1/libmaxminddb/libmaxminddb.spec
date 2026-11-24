# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ca5c87d41339f8bc4daabb53e8a9356b3c995f2d2419b85d7bff823b2ecc252d
%global source1_hash 427183dfeeade52a6a7c6a705745d8662529047ebd6740c2113e5c5c93979e96
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        C library for reading MaxMind DB files
Name:           libmaxminddb
Version:        1.14.1
Release:        %{autorelease}
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://maxmind.github.io/libmaxminddb/
Source0:        https://github.com/maxmind/libmaxminddb/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        maxminddb_config.h
BuildRequires: oreon-rpm-macros
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)

%description
The libmaxminddb library provides a C library for reading MaxMind DB
files, including the GeoIP2 databases from MaxMind. This is a custom
binary format designed to facilitate fast lookups of IP addresses
while allowing for great flexibility in the type of data associated
with an address.

The MaxMind DB format is an open file format. The specification is
available at https://maxmind.github.io/MaxMind-DB/ and licensed under
the Creative Commons Attribution-ShareAlike 3.0 Unported License.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1
autoreconf --force --install

%build
%configure --disable-static
%make_build

%install
%make_install

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.la

mv -f $RPM_BUILD_ROOT%{_includedir}/maxminddb_config{,-%{__isa_bits}}.h
install -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/maxminddb_config.h

%check
LD_PRELOAD=$RPM_BUILD_ROOT%{_libdir}/%{name}.so make check

%files
%license LICENSE
%doc Changes.md README.md
%{_bindir}/mmdblookup
%{_libdir}/%{name}.so.0*
%{_mandir}/man1/mmdblookup.1*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/maxminddb.h
%{_includedir}/maxminddb_config.h
%{_includedir}/maxminddb_config-%{__isa_bits}.h
%{_mandir}/man3/%{name}.3*
%{_mandir}/man3/MMDB_*.3*

%changelog
%autochangelog
