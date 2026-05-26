%bcond stemming %{undefined rhel}

Summary: Utilities to generate, maintain and access the AppStream database
Name:    appstream
Version: 1.1.0
Release: 3%{?dist}

# lib LGPLv2+, tools GPLv2+
License: GPL-2.0-or-later AND LGPL-2.1-or-later
#URL:     http://www.freedesktop.org/wiki/Distributions/AppStream
URL:     https://github.com/ximion/appstream
Source0: https://www.freedesktop.org/software/appstream/releases/AppStream-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 298b4732a2670503328e022d68d6ebbb253c716dad0b6ba127a4065262dd2f2c
%global source0_file AppStream-1.1.0.tar.xz
# oreon url source checksums end

# upstream patches

# upstreamable patches


# needed for cmake auto-provides
BuildRequires: cmake
BuildRequires: meson >= 0.62
BuildRequires: gettext
BuildRequires: git-core
BuildRequires: gperf
BuildRequires: gtk-doc
BuildRequires: intltool
BuildRequires: itstool
%if %{with stemming}
BuildRequires: libstemmer-devel
%endif
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gi-docgen) >= 2021.1
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libfyaml)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(Qt6Core) >= 6.2.4
BuildRequires: pkgconfig(xmlb) >= 0.3.14
BuildRequires: pkgconfig(yaml-0.1)
# lrelease
BuildRequires: qt6-linguist
BuildRequires: sed
BuildRequires: vala
BuildRequires: xmlto

Requires: (appstream-data if PackageKit)

%description
AppStream makes it easy to access application information from the
AppStream database over a nice GObject-based interface.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# -vala subpackage removed in F30
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/AppStream-1.1.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "298b4732a2670503328e022d68d6ebbb253c716dad0b6ba127a4065262dd2f2c" || { echo "oreon: Source0 SHA256 mismatch for AppStream-1.1.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n AppStream-%{version} -S git_am


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
# move metainfo to right/legacy location
mkdir -p %{buildroot}%{_kf5_metainfodir}
mv %{buildroot}%{_datadir}/metainfo/*.xml \
   %{buildroot}%{_metainfodir}
%endif


%check
%{meson_test} ||:


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
%{_datadir}/appstream/
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/AppStream-1.0.typelib
%{_libdir}/libappstream.so.5
%{_libdir}/libappstream.so.%{version}
%{_metainfodir}/org.freedesktop.appstream.cli.*.xml
# put in -devel? -- rex
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
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/AppStream-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/appstream.deps
%{_datadir}/vala/vapi/appstream.vapi
%{_docdir}/appstream/html/
## symlink pointing to ^^, but need to take care, since rpm has
## trouble replacing dirs with symlinks, omit it for now -- rex
%exclude %{_datadir}/gtk-doc/html/appstream
# Maybe this should be split out? -- ngompa
%{_datadir}/installed-tests/appstream/metainfo-validate.test

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


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-3
- Prepare for Oreon 11 (RP1)
