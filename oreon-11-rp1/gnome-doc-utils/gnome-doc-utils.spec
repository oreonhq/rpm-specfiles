%global source0_hash cb0639ffa9550b6ddf3b62f3b1add92fb92ab4690d351f2353cffe668be8c4a6

Name: gnome-doc-utils
Version: 0.20.10
Release: 45%{?dist}
Summary: Documentation utilities for GNOME

License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GFDL-1.1-or-later
URL:     https://wiki.gnome.org/Projects/GnomeDocUtils
Source:  https://download.gnome.org/sources/%{name}/0.20/%{name}-%{version}.tar.xz
#VCS: git:git://git.gnome.org/gnome-doc-utils
# RH bug #438638 / GNOME bug #524207
Patch1:  gnome-doc-utils-0.14.0-package.patch
Patch2:  gnome-doc-utils-0.20.10-python3.patch
Patch3:  gnome-doc-utils-0.20.10-configure-py312.patch

BuildArch: noarch

BuildRequires: gcc
BuildRequires: libxml2-devel >= 2.6.12
BuildRequires: libxslt-devel >= 1.1.8
BuildRequires: python3-libxml2
BuildRequires: python3-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: make

Requires: libxml2 >= 2.6.12
Requires: libxslt >= 1.1.8
Requires: python3-libxml2
# for /usr/share/aclocal
Requires: automake
# for /usr/share/gnome/help
#Requires: yelp
# Currently creates a chicken/egg problem; gnome-doc-utils is needed in
# the build-chain for yelp, thus making it nearly impossible to ever
# update yelp for say newer Firefox.
Requires: gnome-doc-utils-stylesheets = %{version}-%{release}

%description
gnome-doc-utils is a collection of documentation utilities for the GNOME
project. Notably, it contains utilities for building documentation and
all auxiliary files in your source tree.

# note that this is an "inverse dependency" subpackage
%package stylesheets
Summary: XSL stylesheets used by gnome-doc-utils
License: LGPL-2.0-or-later
# for the validation with xsltproc to use local dtds
Requires: docbook-dtds
# for /usr/share/pkgconfig
Requires: pkgconfig
# for /usr/share/xml
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

%files -f %{name}.lang
%doc AUTHORS README NEWS
%license COPYING COPYING.GPL COPYING.LGPL
%{_bindir}/*
%{_datadir}/aclocal/gnome-doc-utils.m4
%{_datadir}/gnome/help/gnome-doc-make
%{_datadir}/gnome/help/gnome-doc-xslt
%{_datadir}/gnome-doc-utils
%{_mandir}/man1/xml2po.1*
%{python3_sitelib}/xml2po/
%{_datadir}/pkgconfig/gnome-doc-utils.pc
%{_datadir}/pkgconfig/xml2po.pc

%files stylesheets
%{_datadir}/xml/gnome
%{_datadir}/xml/mallard

%changelog
%autochangelog
