# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4460c20cfcf68b994a5ee206ed15fc19ad312f16c96075186e83b0e3f4aa48a5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

Name:           wayland-protocols
Version:        1.50
Release:        1%{?dist}
Summary:        Wayland protocols that adds functionality not available in the core protocol

License:        MIT
URL:            https://wayland.freedesktop.org/
Source0:        https://gitlab.freedesktop.org/wayland/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.sig
# Daniel Stone, A66D805F7C9329B4C5D82767CCC4F07FAC641EFF
Source2:        gpgkey-A66D805F7C9329B4C5D82767CCC4F07FAC641EFF.gpg

BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  wayland-devel >= 1.25.0

%description
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

%package devel
Summary:        Wayland protocols that adds functionality not available in the core protocol
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
wayland-protocols contains Wayland protocols that adds functionality not
available in the Wayland core protocol. Such protocols either adds
completely new functionality, or extends the functionality of some other
protocol either in Wayland core, or some other protocol in
wayland-protocols.

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

%files devel
%license COPYING
%doc README.md
%{_datadir}/pkgconfig/%{name}.pc
%{_datadir}/%{name}/
%{_includedir}/%{name}/

%changelog
%autochangelog
