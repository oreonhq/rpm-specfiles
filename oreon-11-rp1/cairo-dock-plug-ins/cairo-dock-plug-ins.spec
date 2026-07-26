%global source0_hash 751251bbc49f8381a7d3375f071afe62d752b2ead20bc8e0690cfcc94b814ab3

%global	urlver		3.6
%global	mainver		3.6.2

%global	core_least_ver	3.6.0

%dnl %global	use_git	1
%global	gitdate	20250922
%global	githash	f45372c1fbce5dc9a34a991ff6e2485d39603279
%global	shorthash	%(c=%{githash} ; echo ${c:0:7})

%global	tarballver	%{mainver}%{?use_git:-%{gitdate}git%{shorthash}}

%global	baserelease	3
%dnl %global	alphatag		.rc9

%global	ruby_vendorlib	%(ruby -rrbconfig -e "puts RbConfig::CONFIG['vendorlibdir']")
%global	dbus_datadir	%{_datadir}/cairo-dock/plug-ins/Dbus

%global	build_unstable	1

%undefine _strict_symbol_defs_build

##########################################
%global		flagrel	%{nil}
%global		use_gcc_strict_sanitize	0

%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
##########################################

Name:			cairo-dock-plug-ins
Version:		%{mainver}%{?use_git:^%{gitdate}git%{shorthash}}
Release:		%{baserelease}%{?alphatag}%{?dist}%{flagrel}
Summary:		Plug-ins files for Cairo-Dock

# SPDX confirmed
License:		GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only
URL:			http://glx-dock.org/
#Source0:		http://launchpad.net/cairo-dock-plug-ins/%%{urlver}/%%{mainver}/+download/cairo-dock-plugins-%%{mainver}.tar.gz
# Some contents removed: see https://bugzilla.redhat.com/show_bug.cgi?id=1178912
Source0:		cairo-dock-plugins-fedora-%{tarballver}.tar.gz
# Source0 is created from Source1
Source1:		cairo-dock-plug-ins-create-fedora-tarball.sh

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	gettext

BuildRequires:	pkgconfig(gldi) >= %{core_least_ver}
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	cairo-dock-devel >= %{core_least_ver}

# Plug-ins
BuildRequires:	pkgconfig(ayatana-indicator3-0.4)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(dbusmenu-glib-0.4)
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	pkgconfig(libical)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libxklavier)
BuildRequires:	pkgconfig(openssl) >= 1.1
# BuildRequires:	pkgconfig(thunar-vfs-1)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(vte-2.91)
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
# Use webkit2gtk-4.1 for F-39+
BuildRequires:	pkgconfig(webkit2gtk-4.1)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zeitgeist-2.0)

BuildRequires:	libetpan-devel
BuildRequires:	lm_sensors-devel

# Bindings
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	ruby-devel
BuildRequires:	vala
BuildRequires:	make

Requires:	%{name}-base%{?_isa} = %{version}-%{release}
# Explicitly write below
Requires:	%{name}-dbus%{?_isa} = %{version}-%{release}
# cairo-dock-launcher-API-daemon is written in python,
# so for now make this depending on python
Requires:	cairo-dock-python3%{?_isa} = %{version}-%{release}
# Require xdg-utils for logout by default
Requires:	xdg-utils

%description
This package is a meta package for Cairo-Dock plugins.

%package	base
Summary:	Base files for Cairo-Dock plugins
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
%if 0%{?fedora} >= 41
Requires:	gdk-pixbuf2-modules-extra
%endif

%description	base
This package contains plug-ins files for Cairo-Dock.

%package	common
Summary:	Common files for Cairo-Dock plugins
BuildArch:	noarch

%description	common
This file contains common files for Cairo-Dock plugins.

%package	dbus
Summary:	Plug-ins files for Cairo-Dock related to Dbus
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	dbus
This package contains plug-ins files for Cairo-Dock related
to Dbus.

%package	xfce
Summary:	Plug-ins files for Cairo-Dock related to Xfce
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	xfce
This package contains plug-ins files for Cairo-Dock related
to Xfce.

%package	kde
Summary:	Plug-ins files for Cairo-Dock related to KDE
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	kde
This package contains plug-ins files for Cairo-Dock related
to KDE.

%package	webkit
Summary:	Plug-ins files for Cairo-Dock related to WebKit
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	webkit
This package contains plug-ins files for Cairo-Dock related
to WebKit.

%package	unstable
Summary:	Unstable plug-ins not installed by default
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}

%description	unstable
This package contains unstable and experimental
plug-ins not installed by default.

%package	-n cairo-dock-python3
Summary:	Python3 binding for Cairo-Dock
Requires:	cairo-dock-core >= %{core_least_ver}
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	python3-gobject
Requires:	python3-dbus
Obsoletes:	cairo-dock-python3 < 3.5.99^20241007git019f49f-1

%description	-n cairo-dock-python3
This package contains Python3 binding files for Cairo-Dock

%package	-n cairo-dock-ruby
Summary:	Ruby binding for Cairo-Dock
Requires:	cairo-dock-core >= %{core_least_ver}
Requires:	%{name}-dbus = %{version}-%{release}
Requires:	ruby(release)
Requires:	rubygem(ruby-dbus)
Requires:	rubygem(parseconfig)
BuildArch:	noarch

%description	-n cairo-dock-ruby
This package contains Ruby binding files for Cairo-Dock

%package	-n cairo-dock-vala
Summary:	Vala binding for Cairo-Dock
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
Requires:	vala

%description	-n cairo-dock-vala
This package contains Vala binding files for Cairo-Dock

%package	-n cairo-dock-vala-devel
Summary:	Development files for Vala binding for Cairo-Dock
Requires:	cairo-dock-vala%{?_isa} = %{version}-%{release}
Requires:	%{name}-dbus%{?isa} = %{version}-%{release}

%description	-n cairo-dock-vala-devel
This package contains development files for Vala
binding for Cairo-Dock.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cairo-dock-plugins-%{mainver}%{?use_git:-%{gitdate}git%{shorthash}}

## permission
# %%_fixperms cannot fix permissions completely here
for dir in */
do
	find $dir -type f | xargs -r chmod 0644
done
chmod 0644 [A-Z]* copyright
chmod 0755 */

# cmake issue
sed -i.debuglevel \
	-e '\@add_definitions@s|-O3|-O2|' \
	CMakeLists.txt
sed -i.stat \
	-e 's|\${MSGFMT_EXECUTABLE}|\${MSGFMT_EXECUTABLE} --statistics|' \
	po/CMakeLists.txt

# Compilation flags
sed -i.wall \
	-e 's|-Wno-all||' \
	Dbus/interfaces/vala/src/CMakeLists.txt

## source code fix
## Bindings
# Ruby
sed -i.site \
	-e "s|CONFIG\['rubylibdir'\]|CONFIG['vendorlibdir']|" \
	CMakeLists.txt
# ????
sed -i.installdir \
	-e '\@REGEX REPLACE.*RUBY@d' \
	-e '\@set.*RUBY_LIB_DIR.*CMAKE_INSTALL_PREFIX.*RUBY_LIB_DIR_INSTALL@d' \
	CMakeLists.txt

# Modify version forcely
%if 0%{?use_git}
sed -i CMakeLists.txt -e '\@set (\(CORE_REQUIRED_\|\)VERSION @s|VERSION.*|VERSION "%{mainver}")|'
%endif

# Kill python2 explicitly
sed -i.py2 CMakeLists.txt -e 's|python2)|python2-nono)|'
# ... and explicitly use python3
env LANG=C grep -rl /usr/bin/env . | \
	xargs sed -i -e 's|/usr/bin/env[ \t]*python$|/usr/bin/python3|'

# Use recent standard
sed -i.std CMakeLists.txt -e 's|-std=gnu99 ||'

%build
%set_build_flags

%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
%endif

rm -f CMakeCache.txt
%cmake \
%if 0%{?build_unstable} >= 1
	-Denable-disks=TRUE \
	-Denable-doncky=TRUE \
	-Denable-global-menu=TRUE \
	-Denable-network-monitor=TRUE \
	-Denable-weblets=TRUE \
%if 0
	-Denable-scooby-do=TRUE \
%endif
%endif

%cmake_build

%install
%cmake_install

# Collect documents
rm -rf documents licenses documents-dbus
mkdir documents licenses documents-dbus
cp -a \
	ChangeLog \
	documents
mkdir documents-dbus/Dbus
cp -a Dbus/demos \
	documents-dbus/Dbus/
cp -a \
	LGPL-2 \
	LICENSE \
	copyright \
	licenses/

# Just to suppress rpmlint...
pushd $RPM_BUILD_ROOT

for f in \
	`find . -name \*.conf`
do
	sed -i -e '1i\ ' $f
done

set +x
for f in \
	.%{_datadir}/cairo-dock/plug-ins/*/* \
	$(find . -name \*.rb)
do
	if head -n 1 $f 2>/dev/null | grep -q /bin/ ; then 
		set -x
		chmod 0755 $f
		set +x
	fi
done

# Modify CDApplet.h not to contain %%buildroot strings
sed -i .%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h \
	-e '\@def@s|__.*\(DBUS_INTERFACES_VALA_SRC_CDAPPLET_H__\)|__\1|'

popd

%find_lang cairo-dock-plugins

%ldconfig_scriptlets -n cairo-dock-vala

%files	common
%license	licenses/*

%files
# This is a metapackage

%files	base -f cairo-dock-plugins.lang
%doc	documents/*

%{_libdir}/cairo-dock/*
%{_datadir}/cairo-dock/plug-ins/*
%{_datadir}/cairo-dock/gauges/*/

%exclude	%{_libdir}/cairo-dock/*weblet*
%exclude	%{_libdir}/cairo-dock/*xfce*
%exclude	%{_libdir}/cairo-dock/*kde*
%exclude	%{_libdir}/cairo-dock/*Dbus*
%exclude	%{_datadir}/cairo-dock/plug-ins/*weblet*
%exclude	%{_datadir}/cairo-dock/plug-ins/*xfce*
%exclude	%{_datadir}/cairo-dock/plug-ins/*kde*
%exclude	%{_datadir}/cairo-dock/plug-ins/Dbus/
%if 0%{?build_unstable} >= 1
%exclude	%{_libdir}/cairo-dock/appmenu-registrar
%exclude	%{_libdir}/cairo-dock/libcd-Global-Menu.so
%exclude	%{_libdir}/cairo-dock/libcd-disks.so
%exclude	%{_libdir}/cairo-dock/libcd-doncky.so
%exclude	%{_libdir}/cairo-dock/libcd-network-monitor.so
#%%exclude	%%{_libdir}/cairo-dock/libcd-scooby-do.so
%exclude	%{_datadir}/cairo-dock/plug-ins/Disks/
%exclude	%{_datadir}/cairo-dock/plug-ins/Doncky/
%exclude	%{_datadir}/cairo-dock/plug-ins/Global-Menu/
%exclude	%{_datadir}/cairo-dock/plug-ins/Network-Monitor/
#%%exclude	%%{_datadir}/cairo-dock/plug-ins/Scooby-Do/
%endif
# Vala
%exclude	%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h

%if 0%{?build_unstable} >= 1
%files	unstable
%{_libdir}/cairo-dock/appmenu-registrar
%{_libdir}/cairo-dock/libcd-Global-Menu.so
%{_libdir}/cairo-dock/libcd-disks.so
%{_libdir}/cairo-dock/libcd-doncky.so
%{_libdir}/cairo-dock/libcd-network-monitor.so
#%%{_libdir}/cairo-dock/libcd-scooby-do.so
%{_datadir}/cairo-dock/plug-ins/Disks/
%{_datadir}/cairo-dock/plug-ins/Doncky/
%{_datadir}/cairo-dock/plug-ins/Global-Menu/
%{_datadir}/cairo-dock/plug-ins/Network-Monitor/
#%%{_datadir}/cairo-dock/plug-ins/Scooby-Do/
%endif

%files	dbus
%doc	documents-dbus/*
%{_libdir}/cairo-dock/*Dbus*
%dir	%{dbus_datadir}
%{dbus_datadir}/CDBashApplet.sh
%{dbus_datadir}/Dbus.conf
%{dbus_datadir}/icon.svg

%files	xfce
%{_libdir}/cairo-dock/*xfce*
%{_datadir}/cairo-dock/plug-ins/*xfce*

%files	kde
%{_libdir}/cairo-dock/*kde*
%{_datadir}/cairo-dock/plug-ins/*kde*

%files	webkit
%{_libdir}/cairo-dock/*weblet*
%{_datadir}/cairo-dock/plug-ins/*weblet*

%files	-n cairo-dock-python3
%{dbus_datadir}/CairoDock.py*
%{dbus_datadir}/CDApplet.py*
%{dbus_datadir}/CDBashApplet.py*
%{dbus_datadir}/__pycache__/

%files	-n cairo-dock-ruby
%{dbus_datadir}/CDApplet.rb

%files -n cairo-dock-vala
%{_libdir}/libCDApplet.so.1*
%{_datadir}/vala/vapi/CDApplet.*

%files -n cairo-dock-vala-devel
%{_libdir}/libCDApplet.so
%{_libdir}/pkgconfig/CDApplet.pc
%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h

%changelog
%autochangelog
