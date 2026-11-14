# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 274b9b919ef3152bfb3da3a13c950dd60d6e2bcd54230ffeca298d03b40d0525
%global source1_hash 5b838ee2b10da2e23b95a665fe4831dc54c62376362f6de2bed8004d60ae2ffb

Name:           libmnl
Version:        1.0.5
Release:        1%{?dist}
Summary:        Minimalistic Netlink user-space library
License:        LGPL-2.1-or-later
URL:            https://netfilter.org/projects/libmnl/
Source0:        https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2
Source1:        https://netfilter.org/projects/libmnl/files/%{name}-%{version}.tar.bz2.sig
Source2:        netfilter-coreteam.asc

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  make

%description
libmnl is a small user-space library for constructing, parsing, and validating
Netlink messages.

%package devel
Summary:        Development files for libmnl
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for developing applications that use libmnl.

%package static
Summary:        Static library for libmnl
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static library for developing applications that use libmnl.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup

%build
%configure --enable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc README
%{_libdir}/libmnl.so.0*

%files devel
%{_includedir}/libmnl/
%{_libdir}/libmnl.so
%{_libdir}/pkgconfig/libmnl.pc

%files static
%{_libdir}/libmnl.a

%changelog
%autochangelog
