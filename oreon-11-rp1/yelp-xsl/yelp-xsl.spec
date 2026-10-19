%global source0_hash 59d43a8f8fe67b784f14f9a04dd4a7a092a7f4a64a65e71b90fe02a47a50fbec
%global tarball_version %(echo %{version} | tr '~' '.')
Name:           yelp-xsl
Version:        49.0
Release:        1%{?dist}
Summary:        XSL stylesheets for the yelp help browser
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:            https://download.gnome.org/sources/yelp-xsl
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/ducktype
BuildRequires:  /usr/bin/xmllint
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  python3-libxml2
# /oreon:deps
%description
This package contains XSL stylesheets that are used by the yelp help browser.

%package devel
Summary: Developer documentation for yelp-xsl
Requires: %{name} = %{version}-%{release}
%description devel
The yelp-xsl-devel package contains developer documentation for the
XSL stylesheets in yelp-xsl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n yelp-xsl-devel -f %{oreon_filedir}/yelp-xsl-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-2
- Import
