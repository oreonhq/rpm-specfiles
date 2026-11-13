# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 59d43a8f8fe67b784f14f9a04dd4a7a092a7f4a64a65e71b90fe02a47a50fbec
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: yelp-xsl
Version: 49.0
Release: 1%{?dist}
Summary: XSL stylesheets for Mallard and DocBook help
License: GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL: https://gitlab.gnome.org/GNOME/yelp-xsl
Source0: https://download.gnome.org/sources/yelp-xsl/49/yelp-xsl-%{version}.tar.xz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: meson
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: gettext

%description
Stylesheets yelp-build uses to turn Mallard and DocBook into HTML.

%prep
%oreon_sha256
%autosetup -n yelp-xsl-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_datadir}/yelp-xsl/
%{_datadir}/pkgconfig/yelp-xsl.pc
