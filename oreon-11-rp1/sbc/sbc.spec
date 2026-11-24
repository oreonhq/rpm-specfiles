# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a1ada76ef35e5af9c2fbd063754dc9e37a8d989417c6eb1ecebb089b1383ae9e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:          sbc
Version:       2.2
Release:        %{autorelease}
Summary:       Sub Band Codec used by bluetooth A2DP

License:       GPL-2.0-only AND LGPL-2.1-or-later
URL:           http://www.bluez.org
Source0:       http://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: libsndfile-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
SBC (Sub Band Codec) is a low-complexity audio codec used in the Advanced Audio 
Distribution Profile (A2DP) bluetooth standard but can be used standalone. It 
uses 4 or 8 subbands, an adaptive bit allocation algorithm in combination with 
an adaptive block PCM quantizers.

%package -n libsbc
Summary: Library for the SBC (Sub Band Codec)

%description -n libsbc
Library for SBC (Sub Band Codec) is a low-complexity audio codec used in the
Advanced Audio Distribution Profile (A2DP) bluetooth standard but can be used
standalone. It uses 4 or 8 subbands, an adaptive bit allocation algorithm in
combination with an adaptive block PCM quantizers.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog
%{_bindir}/sbc*

%files -n libsbc
%license COPYING
%{_libdir}/libsbc.so.1*

%files devel
%{_includedir}/sbc/
%{_libdir}/pkgconfig/sbc.pc
%{_libdir}/libsbc.so

%changelog
%autochangelog
