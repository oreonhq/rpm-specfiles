%global source0_hash 554373deb5b393b9d84b275dd2ca66c9a4a2d0e6ec92044fab8aa53e3032d2b5

%global branch 1.28

Name:          libmateweather
Version:       %{branch}.0
Release:       %autorelease
Summary:       Libraries to allow MATE Desktop to display weather information
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

Patch0:        libmateweather_0001-Update-AviationWeather-URL_1.28.patch

BuildRequires: glib2-devel
BuildRequires: gtk3-devel
BuildRequires: libsoup-devel
BuildRequires: libxml2-devel
BuildRequires: mate-common
BuildRequires: make

Requires:      %{name}-data = %{version}-%{release}

%description
Libraries to allow MATE Desktop to display weather information

%package data
Summary: Data files for the libmateweather
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description data
This package contains shared data needed for libmateweather.

%package devel
Summary:  Development files for libmateweather
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libmateweather

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static           \
           --disable-schemas-compile  \
           --enable-gtk-doc-html

# fix unused-direct-shlib-dependency
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool 

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -fv {} ';'
find %{buildroot} -name '*.a' -exec rm -fv {} ';'

%find_lang %{name} --with-gnome --all-name

%files
%doc AUTHORS COPYING README
%{_datadir}/glib-2.0/schemas/org.mate.weather.gschema.xml
%{_libdir}/libmateweather.so.1*

%files data -f %{name}.lang
%{_datadir}/icons/hicolor/*/status/*
%{_datadir}/libmateweather/

%files devel
%%doc %{_datadir}/gtk-doc/html/libmateweather/
%{_libdir}/libmateweather.so
%{_includedir}/libmateweather/
%{_libdir}/pkgconfig/mateweather.pc

%changelog
%autochangelog
