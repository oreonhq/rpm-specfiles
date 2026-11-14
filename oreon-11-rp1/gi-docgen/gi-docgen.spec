# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 71983c4be79de43290721af1d65d7974ca0ee5892f18d3a62ca814edd5db073f

Name: gi-docgen
Version: 2026.1
Release: 1%{?dist}
Summary: Documentation generator for GObject libraries
License: Apache-2.0 OR GPL-3.0-or-later
URL: https://gitlab.gnome.org/GNOME/gi-docgen
Source0: %{url}/-/archive/%{version}/gi-docgen-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: graphviz
BuildRequires: meson
BuildRequires: python3
BuildRequires: python3-jinja2
BuildRequires: python3-markdown
BuildRequires: python3-markupsafe
BuildRequires: python3-packaging
BuildRequires: python3-pygments
BuildRequires: python3-pytest
BuildRequires: python3-typogrify

Requires: python3-jinja2
Requires: python3-markdown
Requires: python3-markupsafe
Requires: python3-packaging
Requires: python3-pygments
Requires: python3-typogrify
Provides: pkgconfig(gi-docgen) = %{version}

%description
GI-DocGen generates API reference documentation from GObject
Introspection data.

%prep
%oreon_sha256
%autosetup

%build
%meson -Ddevelopment_tests=false
%meson_build

%install
%meson_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} python3 -m pytest -v tests
PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig \
  pkg-config --modversion gi-docgen | grep -Fx %{version}

%files
%license LICENSES/*
%doc CHANGES.md README.md
%{_bindir}/gi-docgen
%{python3_sitelib}/gidocgen/
%{_datadir}/pkgconfig/gi-docgen.pc

%changelog
%autochangelog
