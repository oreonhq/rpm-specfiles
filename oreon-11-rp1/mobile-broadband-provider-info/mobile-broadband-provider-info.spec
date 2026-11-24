# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 89bfeff215f4bff8e9c3ff2ec25250fdb080d11e9bfa59c6fc71982ac01c814a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Mobile broadband provider database
Name: mobile-broadband-provider-info
Version: 20240407
Release: 1%{?dist}
URL: https://wiki.gnome.org/Projects/NetworkManager/MobileBroadband/ServiceProviders
License: CC-PDDC
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: meson
BuildRequires: /usr/bin/xmllint
BuildRequires: /usr/bin/xsltproc

%description
The mobile-broadband-provider-info package contains listings of mobile
broadband (3G) providers and associated network and plan information.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains files necessary for
developing developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%{_datadir}/%{name}
%doc README
%license COPYING

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
