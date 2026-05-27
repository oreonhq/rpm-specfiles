%global source0_hash 94e7096a49c400628ecddcafe313d63bf917d95a90ab994930909de724604e0a

%if 0%{?rhel} >= 10
%bcond_with gtk2
%else
%bcond_without gtk2
%endif

%if 0%{?rhel} >= 9
%bcond_with mono
%else
%bcond_without mono
%endif

Name:		libappindicator
Version:	12.10.1
Release:	10%{?dist}
Summary:	Application indicators library

# Automatically converted from old format: LGPLv2 and LGPLv3 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2 AND LGPL-3.0-only
URL:		https://launchpad.net/libappindicator
# see https://launchpad.net/ubuntu/+source/libappindicator/12.10.1+20.10.20200706.1-0ubuntu1
Source0:	https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/%{name}/%{version}+20.10.20200706.1-0ubuntu1/%{name}_%{version}+20.10.20200706.1.orig.tar.gz
Patch0:		0001_Fix_mono_dir.patch

BuildRequires: make
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	vala
BuildRequires:	dbus-glib-devel
BuildRequires:	libdbusmenu-devel
%if %{with gtk2}
BuildRequires:	libdbusmenu-gtk2-devel
BuildRequires:	gtk2-devel
%endif
BuildRequires:	libdbusmenu-gtk3-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk3-devel
BuildRequires:	libindicator-devel
BuildRequires:	libindicator-gtk3-devel
%if %{with mono}
%ifarch %{mono_arches}
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-sharp2-gapi
BuildRequires:	mono-devel
BuildRequires:	mono-nunit-devel
%endif
%endif

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
# Parallel make, crash the build
make -j1 V=1
popd
%endif

pushd build-gtk3
export CFLAGS="%{optflags} $CFLAGS -Wno-deprecated-declarations"
%configure --with-gtk=3 --enable-gtk-doc --disable-static
# Parallel make, crash the build
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


%if %{with gtk2}
%files
%doc AUTHORS README COPYING COPYING.LGPL.2.1
%{_libdir}/libappindicator.so.*


%files devel
%dir %{_includedir}/libappindicator-0.1/
%dir %{_includedir}/libappindicator-0.1/libappindicator/
%{_includedir}/libappindicator-0.1/libappindicator/*.h
%{_libdir}/libappindicator.so
%{_libdir}/pkgconfig/appindicator-0.1.pc
%endif


%files gtk3
%doc AUTHORS README COPYING COPYING.LGPL.2.1
%{_libdir}/libappindicator3.so.*
%{_libdir}/girepository-1.0/AppIndicator3-0.1.typelib


%files gtk3-devel
%dir %{_includedir}/libappindicator3-0.1/
%dir %{_includedir}/libappindicator3-0.1/libappindicator/
%{_includedir}/libappindicator3-0.1/libappindicator/*.h
%{_libdir}/libappindicator3.so
%{_libdir}/pkgconfig/appindicator3-0.1.pc
%{_datadir}/gir-1.0/AppIndicator3-0.1.gir
%{_datadir}/vala/vapi/appindicator3-0.1.vapi
%{_datadir}/vala/vapi/appindicator3-0.1.deps


%files docs
%doc %{_datadir}/gtk-doc/html/libappindicator/


%if %{with mono}
%ifarch %{mono_arches}
%files sharp
%doc AUTHORS README COPYING COPYING.LGPL.2.1
%dir %{_libdir}/appindicator-sharp-0.1/
%{_libdir}/appindicator-sharp-0.1/appindicator-sharp.dll
%{_libdir}/appindicator-sharp-0.1/appindicator-sharp.dll.config
%{_libdir}/appindicator-sharp-0.1/policy.0.0.appindicator-sharp.config
%{_libdir}/appindicator-sharp-0.1/policy.0.0.appindicator-sharp.dll
%{_libdir}/appindicator-sharp-0.1/policy.0.1.appindicator-sharp.config
%{_libdir}/appindicator-sharp-0.1/policy.0.1.appindicator-sharp.dll
%dir %{_prefix}/lib/mono/appindicator-sharp/
%{_prefix}/lib/mono/appindicator-sharp/appindicator-sharp.dll
%{_prefix}/lib/mono/appindicator-sharp/policy.0.0.appindicator-sharp.dll
%dir %{_prefix}/lib/mono/gac/appindicator-sharp/
%dir %{_prefix}/lib/mono/gac/appindicator-sharp/*/
%{_prefix}/lib/mono/gac/appindicator-sharp/*/appindicator-sharp.dll
%{_prefix}/lib/mono/gac/appindicator-sharp/*/appindicator-sharp.dll.config
%dir %{_prefix}/lib/mono/gac/policy.0.0.appindicator-sharp/
%dir %{_prefix}/lib/mono/gac/policy.0.0.appindicator-sharp/*/
%{_prefix}/lib/mono/gac/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.dll
%{_prefix}/lib/mono/gac/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.config


%files sharp-devel
%{_libdir}/pkgconfig/appindicator-sharp-0.1.pc

%endif
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.10.1-10
- Prepare for Oreon 11 (RP1)
