%global source0_hash 7df664fd3ad3b1640c6a0ff77fa84f9fabe264111bf1fe8f5df3444d6d4caaca
%bcond stemming %{undefined rhel}
Summary:        Utilities to generate, maintain and access the AppStream database
Name:    appstream
Version: 1.2.1
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://github.com/ximion/appstream
Source0:        https://www.freedesktop.org/software/appstream/releases/AppStream-%{version}.tar.xz
%if %{with stemming}
%endif
Requires: (appstream-data if PackageKit)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libstemmer-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libblake3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libfyaml)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(vips)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  qt6-linguist
BuildRequires:  sed
BuildRequires:  vala
BuildRequires:  xmlto
# /oreon:deps
%description
AppStream makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: appstream-vala < 0.12.4-3
Provides: appstream-vala = %{version}-%{release}
%description devel
%{summary}.

%package compose
Summary: Library for generating AppStream data
Requires: %{name}%{?_isa} = %{version}-%{release}
%description compose
%{summary}.

%package compose-devel
Summary:  Development files for %{name}-compose library
Requires: %{name}-compose%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description compose-devel
%{summary}.

%package qt
Summary: Qt6 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description qt
%{summary}.

%package qt-devel
Summary:  Development files for %{name}-qt bindings
Requires: %{name}-qt%{?_isa} = %{version}-%{release}
Requires: pkgconfig(Qt6Core) >= 6.2.4
%description qt-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir AppStream-%{version}
%oreon_prep
%build

%{meson} \
 -Dcompose=true \
 -Dqt=true \
 -Dstemming=%{?with_stemming:true}%{!?with_stemming:false} \
 -Dvapi=true
%{meson_build}
%install
%{meson_install}
mkdir -p %{buildroot}/var/cache/swcatalog/{icons,gv,xml}
touch %{buildroot}/var/cache/swcatalog/cache.watch
%find_lang appstream
%if "%{?_metainfodir}" != "%{_datadir}/metainfo"
mkdir -p %{buildroot}%{_kf5_metainfodir}
mv %{buildroot}%{_datadir}/metainfo/*.xml \
   %{buildroot}%{_metainfodir}
%oreon_autofiles appstream-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles appstream-compose usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles appstream-compose-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles appstream-qt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles appstream-qt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%{meson_test} ||:
%posttrans

%{_bindir}/appstreamcli refresh --force >& /dev/null ||:
%transfiletriggerin -- %{_datadir}/swcatalog/xml
%{_bindir}/appstreamcli refresh --force >& /dev/null ||:
%transfiletriggerpostun -- %{_datadir}/swcatalog/xml
%{_bindir}/appstreamcli refresh --force >& /dev/null ||:
%files -f %{oreon_filedir}/main.list
%files -n appstream-devel -f %{oreon_filedir}/appstream-devel.list
%files -n appstream-compose -f %{oreon_filedir}/appstream-compose.list
%files -n appstream-compose-devel -f %{oreon_filedir}/appstream-compose-devel.list
%files -n appstream-qt -f %{oreon_filedir}/appstream-qt.list
%files -n appstream-qt-devel -f %{oreon_filedir}/appstream-qt-devel.list

%changelog

%autochangelog
