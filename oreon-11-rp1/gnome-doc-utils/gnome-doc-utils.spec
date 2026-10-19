%global source0_hash cb0639ffa9550b6ddf3b62f3b1add92fb92ab4690d351f2353cffe668be8c4a6
Name: gnome-doc-utils
Version: 0.20.10
Release:        45%{?dist}
Summary:        Documentation utilities for GNOME
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GFDL-1.1-or-later
URL:     https://wiki.gnome.org/Projects/GnomeDocUtils
Source0:        https://download.gnome.org/sources/%{name}/0.20/%{name}-%{version}.tar.xz
Patch1:  gnome-doc-utils-0.14.0-package.patch
Patch2:  gnome-doc-utils-0.20.10-python3.patch
Patch3:  gnome-doc-utils-0.20.10-configure-py312.patch
BuildArch: noarch
Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.1.8
Requires: python3-libxml2
Requires: automake
Requires: gnome-doc-utils-stylesheets = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-libxml2
# /oreon:deps
%description
gnome-doc-utils is a collection of documentation utilities for the GNOME
project. Notably, it contains utilities for building documentation and
all auxiliary files in your source tree.

# note that this is an "inverse dependency" subpackage
%package stylesheets
Summary: XSL stylesheets used by gnome-doc-utils
License: LGPL-2.0-or-later
Requires: docbook-dtds
Requires: pkgconfig
Requires: xml-common
%description stylesheets
The gnome-doc-utils-stylesheets package contains XSL stylesheets which
are used by the tools in gnome-doc-utils and by yelp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .package
%patch -P2 -p1 -b .python3
%patch -P3 -p1 -b .python312

%build

%configure --disable-scrollkeeper --enable-build-utils
%make_build
sed -i s/python$/python3/g xml2po/xml2po/xml2po
%install
%make_install
sed -i -e '/^Requires:/d' %{buildroot}%{_datadir}/pkgconfig/xml2po.pc
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-doc-utils-stylesheets -f %{oreon_filedir}/gnome-doc-utils-stylesheets.list

%changelog

%autochangelog
