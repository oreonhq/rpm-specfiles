# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c97abc3409f8fa396b4462b2bb7f147a3a47a4ddc97cfa0b2f18890c9cfde8b0
%global source1_hash 8412a7ccd9e37e44d26ff49f437a5ac1f7711e080fe574deb48ad2671f927b72
%global source2_hash 961f5e8d3dcffab4c04c891a3f26e27bedf49301e53cbf83660001de3d9390c8
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libnftnl
Version:        1.3.2
Release:        %{autorelease}
Summary:        Library for low-level interaction with nftables Netlink's API over libmnl

License:        GPL-2.0-or-later
URL:            https://netfilter.org/projects/libnftnl/
Source0:        %{url}/files/%{name}-%{version}.tar.xz
Source1:        %{url}/files/%{name}-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt

BuildRequires: oreon-rpm-macros
BuildRequires:  libmnl-devel
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gnupg2

%description
A library for low-level interaction with nftables Netlink's API over libmnl.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules
%make_build

%check
%make_build check

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING
%{_libdir}/*.so.*

%files devel
%{_libdir}/libnft*.so
%{_libdir}/pkgconfig/libnftnl.pc
%{_includedir}/libnftnl

%changelog
%autochangelog
