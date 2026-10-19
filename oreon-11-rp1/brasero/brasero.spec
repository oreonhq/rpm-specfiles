%global source0_hash 3226049ac40969093c5756f9892e76dbda1efeb105cda32f39fd52f6547ed5b3
%define basever %(echo %{version} | sed "s/\.[0-9]*$//")
%bcond cdrdao %[!(0%{?rhel} >= 9)]
%bcond cdrkit %[!(0%{?rhel} >= 9)]
%bcond dvdrwtools %[!(0%{?rhel} >= 9)]
%bcond nautilus %[!(0%{?fedora} >= 37 || 0%{?rhel} >= 10)]
%bcond plparser %[!(0%{?rhel} >= 10)]
Name:      brasero
Version:   3.12.4
Release:        1%{?dist}
Summary:        Gnome CD/DVD burning application
License:   GPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-2.0-only AND CC-BY-SA-2.0 AND GPL-2.0-or-later WITH GStreamer-exception-2008
URL:       https://wiki.gnome.org/Apps/Brasero
Source0:        https://download.gnome.org/sources/%{name}/%{basever}/%{name}-%{version}.tar.xz
%if %{with nautilus}
%endif
%if %{with plparser}
%endif
%{?with_dvdrwtools:Requires:  dvd+rw-tools}
%{?with_cdrkit:Requires:  wodim}
%{?with_cdrkit:Requires:  genisoimage}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%ifnarch s390x
%{?with_cdrdao:Requires:  cdrdao}
%endif
%{?with_cdrkit:Recommends: icedax}
%if %{without nautilus}
Obsoletes: %{name}-nautilus < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libburn-1)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libisofs-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(totem-plparser)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  yelp-tools
# /oreon:deps
%description
Simple and easy to use CD/DVD burning application for the Gnome
desktop.

%package   libs
Summary:   Libraries for %{name}
%description libs
The %{name}-libs package contains the runtime shared libraries for
%{name}.

%if %{with nautilus}
%package   nautilus
Summary:   Nautilus extension for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description nautilus
The %{name}-nautilus package contains the brasero nautilus extension.
%endif

%package   devel
Summary:   Headers for developing programs that will use %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
This package contains the static libraries and header files needed for
developing brasero applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure \
        %{!?with_nautilus:--disable-nautilus} \
        --enable-libburnia \
        --enable-search \
        %{!?with_plparser:--disable-playlist} \
        --enable-preview \
        --enable-inotify \
        %{!?with_cdrdao:--disable-cdrdao} \
        %{!?with_cdrkit:--disable-cdrkit} \
        %{!?with_dvdrwtools:--disable-growisofs} \
        --disable-caches \
        --disable-static
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
%find_lang %{name}
appstream-util replace-screenshots $RPM_BUILD_ROOT%{_datadir}/metainfo/brasero.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/a.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/b.png \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/brasero/c.png
%oreon_autofiles brasero-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brasero-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n brasero-libs -f %{oreon_filedir}/brasero-libs.list
%files -n brasero-devel -f %{oreon_filedir}/brasero-devel.list

%changelog

%autochangelog
