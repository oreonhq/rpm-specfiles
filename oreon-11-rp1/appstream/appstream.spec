# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2624f967068427edc94f3979edae3571bb077063f5bc231f737776da527bf467
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond blake3 1
%bcond stemming 1

Summary: Utilities to generate, maintain and access the AppStream database
Name: appstream
Version: 1.1.3
Release: 2%{?dist}
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/ximion/appstream
Source0: https://www.freedesktop.org/software/appstream/releases/AppStream-%{version}.tar.xz
Source1: AppStream-%{version}.tar.xz.asc
# Matthias Klumpp release key
Source2: gpgkey-D33A3F0CA16B0ACC51A60738494C8A5FBF4DECEB.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: docbook5-style-xsl
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: gperf
BuildRequires: itstool
BuildRequires: libxslt
BuildRequires: meson >= 0.62
%bcond_with rich_ui
%if %{with rich_ui}
BuildRequires: gtk-doc
BuildRequires: qt6-linguist
BuildRequires: vala
%if %{with stemming}
BuildRequires: libstemmer-devel
%endif
%if %{with blake3}
BuildRequires: pkgconfig(libblake3)
%endif
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gi-docgen) >= 2021.1
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(Qt6Core) >= 6.2.4
%endif
BuildRequires: pkgconfig(bash-completion)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libfyaml)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(xmlb) >= 0.3.14
BuildRequires: pkgconfig(yaml-0.1)

Requires: (appstream-data if (PackageKit or libdnf5-plugin-appstream))

%description
AppStream makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(appstream) = %{version}
%if %{without bootstrap}
Provides: appstream-vala = %{version}-%{release}
%endif

%description devel
Development files for %{name}.

%if %{without bootstrap}
%package compose
Summary: Library for generating AppStream data
Requires: %{name}%{?_isa} = %{version}-%{release}

%description compose
Library and tool for generating AppStream data.

%package compose-devel
Summary: Development files for %{name}-compose library
Requires: %{name}-compose%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(appstream-compose) = %{version}

%description compose-devel
Development files for the %{name}-compose library.

%package qt
Summary: Qt6 bindings for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description qt
Qt6 bindings for %{name}.

%package qt-devel
Summary: Development files for %{name}-qt bindings
Requires: %{name}-qt%{?_isa} = %{version}-%{release}
Requires: pkgconfig(Qt6Core) >= 6.2.4

%description qt-devel
Development files for the %{name}-qt bindings.
%endif

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -n AppStream-%{version} -p1

%build
%meson \
%if %{with bootstrap}
 -Dcompose=false \
 -Dqt=false \
 -Dvapi=false \
 -Dgir=false \
 -Ddocs=false \
 -Dapidocs=false \
 -Dblake3-support=false \
 -Dstemming=false \
%else
 -Dcompose=true \
 -Dqt=true \
 -Dvapi=true \
 -Dblake3-support=%{?with_blake3:true}%{!?with_blake3:false} \
 -Dstemming=%{?with_stemming:true}%{!?with_stemming:false} \
%endif
 %{nil}
%meson_build

%install
%meson_install

mkdir -p %{buildroot}/var/cache/swcatalog/{icons,gv,xml}
touch %{buildroot}/var/cache/swcatalog/cache.watch

%find_lang appstream

%check
%meson_test

%posttrans
%{_bindir}/appstreamcli refresh --force >& /dev/null ||:

%transfiletriggerin -- %{_datadir}/swcatalog/xml
%{_bindir}/appstreamcli refresh --force >& /dev/null ||:

%transfiletriggerpostun -- %{_datadir}/swcatalog/xml
%{_bindir}/appstreamcli refresh --force >& /dev/null ||:

%files -f appstream.lang
%doc AUTHORS
%license COPYING
%{_bindir}/appstreamcli
%{_mandir}/man1/appstreamcli.1*
%{_datadir}/bash-completion/completions/appstreamcli
%{_datadir}/appstream/
%if %{without bootstrap}
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/AppStream-1.0.typelib
%endif
%{_libdir}/libappstream.so.5
%{_libdir}/libappstream.so.%{version}
%{_metainfodir}/org.freedesktop.appstream.cli.*.xml
%{_datadir}/gettext/its/metainfo.*
%ghost /var/cache/swcatalog/cache.watch
%dir /var/cache/swcatalog/
%dir /var/cache/swcatalog/icons/
%dir /var/cache/swcatalog/gv/
%dir /var/cache/swcatalog/xml/

%files devel
%{_includedir}/appstream/
%{_libdir}/libappstream.so
%{_libdir}/pkgconfig/appstream.pc
%if %{without bootstrap}
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/AppStream-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/appstream.deps
%{_datadir}/vala/vapi/appstream.vapi
%{_docdir}/appstream/html/
%exclude %{_datadir}/gtk-doc/html/appstream
%{_datadir}/installed-tests/appstream/metainfo-validate.test
%endif

%if %{without bootstrap}
%files compose
%{_libexecdir}/appstreamcli-compose
%{_mandir}/man1/appstreamcli-compose.1*
%{_libdir}/libappstream-compose.so.0
%{_libdir}/libappstream-compose.so.%{version}
%{_libdir}/girepository-1.0/AppStreamCompose-1.0.typelib
%{_metainfodir}/org.freedesktop.appstream.compose.metainfo.xml

%files compose-devel
%{_includedir}/appstream-compose/
%{_libdir}/libappstream-compose.so
%{_libdir}/pkgconfig/appstream-compose.pc
%{_datadir}/gir-1.0/AppStreamCompose-1.0.gir
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/appstream-compose

%files qt
%{_libdir}/libAppStreamQt.so.3
%{_libdir}/libAppStreamQt.so.%{version}

%files qt-devel
%{_includedir}/AppStreamQt/
%{_libdir}/cmake/AppStreamQt/
%{_libdir}/libAppStreamQt.so
%endif

%changelog
%autochangelog
