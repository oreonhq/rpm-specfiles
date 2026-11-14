# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3e496a4020d4145b99fd508a25fa09336a503a4e8900028421e72c6a4b11f905
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: yelp-tools
Version: 42.1
Release: 1%{?dist}
Summary: Tools for building Mallard and DocBook help
License: GPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/yelp-tools
Source0: https://download.gnome.org/sources/yelp-tools/42/yelp-tools-%{version}.tar.xz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: meson
BuildRequires: python3-lxml
BuildRequires: pkgconfig(yelp-xsl)
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: libxml2
Requires: python3-lxml
Requires: yelp-xsl
Requires: itstool
Requires: libxslt

%description
yelp-build turns Ducktype and Mallard documents into HTML. dbus design docs use it.

%prep
%oreon_sha256
%autosetup -n yelp-tools-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_bindir}/yelp-build
%{_bindir}/yelp-check
%{_bindir}/yelp-new
%{_datadir}/yelp-tools/
%{_datadir}/aclocal/yelp.m4
