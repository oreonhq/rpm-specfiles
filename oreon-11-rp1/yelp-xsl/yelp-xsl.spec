%global source0_hash none

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           yelp-xsl
Version:        49.0
Release:        2%{?dist}
Summary:        XSL stylesheets for the yelp help browser

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND BSD-3-Clause
URL:            https://download.gnome.org/sources/yelp-xsl
Source0:        https://download.gnome.org/sources/%{name}/42/%{name}-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  gettext-devel
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  python3-libxml2
BuildRequires:  /usr/bin/ducktype
BuildRequires:  /usr/bin/xmllint
BuildRequires:  /usr/bin/xsltproc

%description
This package contains XSL stylesheets that are used by the yelp help browser.


%package devel
Summary: Developer documentation for yelp-xsl
Requires: %{name} = %{version}-%{release}

%description devel
The yelp-xsl-devel package contains developer documentation for the
XSL stylesheets in yelp-xsl.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc AUTHORS README.md
%license COPYING COPYING.GPL COPYING.LGPL
%{_datadir}/yelp-xsl

%files devel
%{_datadir}/pkgconfig/yelp-xsl.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-2
- Import
