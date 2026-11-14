# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6ae77cd937f9cf7d1321d35c116062c4911e8447010a6a713ac4286f7a9d5987

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sover 3

Name:           libdisplay-info
Version:        0.3.0
Release:        1%{?dist}
Summary:        EDID and DisplayID library

License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libdisplay-info
Source0:        %{url}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sig
# Simon Ser, 34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48
Source2:        gpgkey-34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig(hwdata)

%description
%{summary}.

%package        tools
Summary:        Command-line tools for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    tools
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/%{name}.so.%{sover}
%{_libdir}/%{name}.so.%{version}

%files tools
%{_bindir}/di-edid-decode

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
