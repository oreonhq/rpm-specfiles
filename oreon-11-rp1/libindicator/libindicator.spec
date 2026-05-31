%global source0_hash b2d2e44c10313d5c9cd60db455d520f80b36dc39562df079a3f29495e8f9447f

Name:		libindicator
Version:	12.10.1
Release:	32%{?dist}
Summary:	Shared functions for Ayatana indicators

# SPDX confirmed
License:	GPL-3.0-only
URL:		https://launchpad.net/libindicator
Source0:        https://launchpad.net/libindicator/12.10/12.10.1/+download/%{name}-%{version}.tar.gz
# From GLib 2.62
Patch1:	libindicator-12.10.1-glib262-g_define_type_with_private.patch

BuildRequires:	gtk-doc
BuildRequires:	libtool

BuildRequires:	dbus-glib-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gmodule-2.0)

BuildRequires:	gnome-common
BuildRequires:	make

%description
A set of symbols and convenience functions that all Ayatana indicators are
likely to use.


%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package	tools
Summary:	Shared functions for Ayatana indicators - Tools
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	tools
This package contains tools used by the %{name} package, the
Ayatana indicators system.


%package	gtk3
Summary:	GTK+3 build of %{name}

%description gtk3
A set of symbols and convenience functions that all Ayatana indicators
are likely to use. This is the GTK+ 3 build of %{name}, for use
by GTK+ 3 apps.


%package	gtk3-devel
Summary:	Development files for %{name}-gtk3

Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.


%package	gtk3-tools
Summary:	Shared functions for Ayatana indicators - GTK3 Tools

Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description	gtk3-tools
This package contains tools used by the %{name}-gtk3 package, the
Ayatana indicators system. This package contains the builds of the
tools for the GTK+3 build of %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P1 -p2 -b .orig

sed -i.addvar configure.ac \
	-e '\@LIBINDICATOR_LIBS@s|\$LIBM| \$LIBM|'

# http://bazaar.launchpad.net/~indicator-applet-developers/libindicator/trunk.12.10/view/head:/autogen.sh
cat > autogen.sh <<EOF
#!/bin/sh

PKG_NAME="libindicator"

which gnome-autogen.sh || {
	echo "You need gnome-common from GNOME SVN"
	exit 1
}

USE_GNOME2_MACROS=1 \
. gnome-autogen.sh
EOF

NOCONFIGURE=1 \
	sh autogen.sh


%build
%global _configure ../configure

build() {
gtkver=$1

rm -rf build-gtk${gtkver}
mkdir build-gtk${gtkver}
pushd build-gtk${gtkver}

export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"

%configure \
	--with-gtk=${gtkver} \
	--disable-static \
	--disable-silent-rules \
	%{nil}

sed -i libtool -e 's! -shared ! -Wl,--as-needed\0!g'
sed -i libtool -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g'
sed -i libtool -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g'

%make_build
popd

}

build 2
build 3


%install

install() {
gtkver=$1

pushd build-gtk${gtkver}
%make_install
popd

INDICATOR_PKGCONF_NAME=indicator-0.4
if [ $gtkver == 3 ] ; then
	INDICATOR_PKGCONF_NAME=indicator3-0.4
fi

PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
export PKG_CONFIG_PATH
for var in \
	iconsdir \
	indicatordir \
	%{nil}
do
	vardir=$(pkg-config --variable=${var} ${INDICATOR_PKGCONF_NAME})
	mkdir -p %{buildroot}${vardir}
done
}

install 2
install 3

# Ubuntu doesn't package the dummy indicator
rm -f %{buildroot}%{_libdir}/libdummy-indicator*.so

# Remove libtool files
find %{buildroot} -type f -name '*.la' -delete

%ldconfig_scriptlets
%ldconfig_scriptlets gtk3


%files
%doc	AUTHORS
%license	COPYING
%doc	NEWS
%doc	ChangeLog
%{_libdir}/libindicator.so.7{,.*}
%dir %{_datadir}/libindicator/
%dir %{_datadir}/libindicator/icons/
%{_libdir}/indicators/

%files devel
%dir %{_includedir}/libindicator-0.4/
%dir %{_includedir}/libindicator-0.4/libindicator/
%{_includedir}/libindicator-0.4/libindicator/*.h
%{_libdir}/libindicator.so
%{_libdir}/pkgconfig/indicator-0.4.pc


%files tools
%{_libexecdir}/indicator-loader
%{_datadir}/libindicator/80indicator-debugging


%files gtk3
%doc	AUTHORS
%license	COPYING
%doc	NEWS
%doc	ChangeLog

%{_libdir}/libindicator3.so.7{,.*}
%dir	%{_datadir}/libindicator/
%dir	%{_datadir}/libindicator/icons/
%{_libdir}/indicators3/


%files gtk3-devel
%dir	%{_includedir}/libindicator3-0.4/
%dir	%{_includedir}/libindicator3-0.4/libindicator/

%{_includedir}/libindicator3-0.4/libindicator/*.h
%{_libdir}/libindicator3.so
%{_libdir}/pkgconfig/indicator3-0.4.pc


%files gtk3-tools
%{_libexecdir}/indicator-loader3

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 12.10.1-32
- Prepare for Oreon 11 (RP1)
