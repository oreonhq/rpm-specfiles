%global source0_hash 5677f1c162cb2dd967f2ef3a089aa23da8fea59262dd65eb6dabcd8a9fe86525
Name:           viking
%global forgeurl https://github.com/viking-gps/viking
%global version0 1.11
%global tag0 viking-%version0
%forgemeta
Version:        %forgeversion
Release:        1%{?dist}
Summary:        GPS data editor and analyzer
License:        GPL-2.0-or-later
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{name}-%{version0}/%{name}-%{name}-%{version0}.tar.gz
ExcludeArch:    s390x %{ix86}
Requires:       hicolor-icon-theme
Requires:       gpsbabel
Requires:       expect
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  bzip2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  expat-devel
BuildRequires:  file-devel
BuildRequires:  gcc-c++
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  geoclue2-devel
BuildRequires:  gettext
BuildRequires:  gnome-doc-utils
BuildRequires:  gpsd-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexif-devel
BuildRequires:  libgexiv2-devel
BuildRequires:  libnova-devel
BuildRequires:  liboauth-devel
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  mapnik-devel
BuildRequires:  nettle-devel
BuildRequires:  rarian-compat
BuildRequires:  sqlite-devel
BuildRequires:  xxd
BuildRequires:  yelp-tools
# /oreon:deps
%description
Viking is a free/open source program to manage GPS data. You can import, plot
and create tracks, routes and waypoints, show OSM, Bing Aerial and other maps,
geotag images, create routes using OSRM, see real-time GPS position, make maps
using Mapnik, control items, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup
NOCONFIGURE=1 ./autogen.sh
# Convert TODO to utf-8
mv TODO timestamp
iconv -f ISO-8859-1 -t UTF-8 -o TODO timestamp
touch -r timestamp TODO

%build

%configure
%make_build CFLAGS="${RPM_OPT_FLAGS} -fcommon"
%install
%make_install
find %{buildroot} -name '*.a' -exec rm -f {} ';'
desktop-file-install \
    --add-category="GTK;Network;" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
