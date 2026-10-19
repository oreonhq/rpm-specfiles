%global source0_hash 18e457298abb1c617187361109eeae769317686303fc07726af31e11519c5938
Name:		glabels
Version:	3.4.1
Release:        29%{?dist}
Summary:        A program for creating labels and business cards for GNOME
License:	GPL-3.0-or-later AND LGPL-3.0-or-later AND CC-BY-NC-SA-3.0 AND X11
URL:		https://www.glabels.org
Source0:        https://download.gnome.org/sources/glabels/3.4/glabels-%{version}.tar.xz
Patch01:	glabels-externs.patch
Patch02:	incompatible-pointer-types.patch
Patch03:	xml2-changes.patch
%if ! 0%{?flatpak}
%endif
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}-templates = %{version}-%{release}
Obsoletes:	%{name}-doc < 3.4.1-20
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  barcode-static
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libiec16022)
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  yelp-tools
# /oreon:deps
%description
gLabels is a lightweight program for creating labels and
business cards for the GNOME desktop environment.
It is designed to work with various laser/ink-jet peel-off
label and business card sheets that you'll find at most office
supply stores.

%package	devel
Summary:	Development files and documentation for %{name}
License:	LGPL-3.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
This package contains the header files and development documentation for
libglabels. 

%package 	libs
License:	LGPL-3.0-or-later
Summary:	Development files and documentation for %{name}
Requires:	%{name}-templates = %{version}-%{release}
%description	libs
This package contains the shared libraries for %{name}. 

%package 	templates
License:	MIT
Summary:	The %{name} template database 
BuildArch:	noarch
%description	templates
This package contains the template database for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

%build

%configure --enable-gtk-doc --disable-static
%make_build
%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/glabels-3.0.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/glabels-3.appdata.xml
%find_lang glabels-3.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n glabels-devel -f %{oreon_filedir}/glabels-devel.list
%files -n glabels-libs -f %{oreon_filedir}/glabels-libs.list
%files -n glabels-templates -f %{oreon_filedir}/glabels-templates.list

%changelog

%autochangelog
