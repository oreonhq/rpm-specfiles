%global source0_hash 94e7096a49c400628ecddcafe313d63bf917d95a90ab994930909de724604e0a
%bcond_without gtk2
%bcond_without mono
Name:		libappindicator
Version:	12.10.1
Release:        10%{?dist}
Summary:        Application indicators library
License:	LicenseRef-Callaway-LGPLv2 AND LGPL-3.0-only
URL:		https://launchpad.net/libappindicator
Source0:        https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/%{name}/%{version}+20.10.20200706.1-0ubuntu1/%{name}_%{version}+20.10.20200706.1.orig.tar.gz
Patch0:		0001_Fix_mono_dir.patch
%if %{with gtk2}
%endif
%if %{with mono}
%ifarch %{mono_arches}
%endif
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libdbusmenu-devel
BuildRequires:  libdbusmenu-gtk2-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  libindicator-devel
BuildRequires:  libindicator-gtk3-devel
BuildRequires:  make
BuildRequires:  vala
# /oreon:deps
%description
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%if %{with gtk2}
%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	libdbusmenu-devel
%description devel
This package contains the development files for the appindicator library.
%endif

%package gtk3
Summary:	Application indicators library - GTK 3
%description gtk3
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

This package contains the GTK 3 version of this library.

%package gtk3-devel
Summary:	Development files for %{name}-gtk3
Requires:	%{name}-gtk3 = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	libdbusmenu-devel
%description gtk3-devel
This package contains the development files for the appindicator-gtk3 library.

%package docs
Summary:	Documentation for %{name} and %{name}-gtk3
BuildArch:	noarch
%description docs
This package contains the documentation for the appindicator and
appindicator-gtk3 libraries.

%if %{with mono}
%ifarch %{mono_arches}
%package sharp
Summary:	Application indicators library - C#
Requires: mono-complete
%description sharp
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

This package contains the Mono C# bindings for this library.

%package sharp-devel
Summary:	Development files for %{name}-sharp
Requires:	%{name}-sharp = %{version}-%{release}
%description sharp-devel
This package contains the development files for the appindicator-sharp library.
%endif
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
%patch -P0 -p1 -b .monodir

sed -i "s#mono-csc#mcs#g" configure.ac
# fix for gtk-doc 1.26
sed -i 's/--nogtkinit//' docs/reference/Makefile.am
gtkdocize --copy
cp -f gtk-doc.make gtk-doc.local.make
autoreconf -vif

%build

%global _configure ../configure
mkdir build-gtk2 build-gtk3
%if %{with gtk2}
pushd build-gtk2
export CFLAGS="%{optflags} $CFLAGS -Wno-deprecated-declarations -Wno-error"
%configure --with-gtk=2 --enable-gtk-doc --disable-static
make -j1 V=1
popd
%endif
pushd build-gtk3
export CFLAGS="%{optflags} $CFLAGS -Wno-deprecated-declarations"
%configure --with-gtk=3 --enable-gtk-doc --disable-static
make -j1 V=1
popd
%install
%if %{with gtk2}
pushd build-gtk2
make install DESTDIR=%{buildroot}
popd
%endif
pushd build-gtk3
make install DESTDIR=%{buildroot}
popd
find %{buildroot} -type f -name '*.la' -delete
%if %{with gtk2}
%ldconfig_scriptlets
%endif
%ldconfig_scriptlets gtk3
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%if %{with gtk2}
%files -f %{oreon_filedir}/main.list
%files -n libappindicator-devel -f %{oreon_filedir}/libappindicator-devel.list
%files -n libappindicator-gtk3 -f %{oreon_filedir}/libappindicator-gtk3.list
%files -n libappindicator-gtk3-devel -f %{oreon_filedir}/libappindicator-gtk3-devel.list
%files -n libappindicator-docs -f %{oreon_filedir}/libappindicator-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.10.1-10
- Prepare for Oreon 11 (RP1)
%endif
