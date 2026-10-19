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
%global		flagrel	%{nil}
%global		use_gcc_strict_sanitize	0
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
Name:			cairo-dock-plug-ins
Version:		%{mainver}%{?use_git:^%{gitdate}git%{shorthash}}
Release:        3%{?dist}
Summary:        Plug-ins files for Cairo-Dock
License:		GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-2.0-only
URL:			http://glx-dock.org/
Source0:        cairo-dock-plugins-fedora-%{version}.tar.gz
Source1:		cairo-dock-plug-ins-create-fedora-tarball.sh
Requires:	%{name}-base%{?_isa} = %{version}-%{release}
Requires:	%{name}-dbus%{?_isa} = %{version}-%{release}
Requires:	cairo-dock-python3%{?_isa} = %{version}-%{release}
Requires:	xdg-utils
# oreon:deps
BuildRequires:  cairo-dock-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libetpan-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gldi)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-vfs-2.0)
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libgnomeui-2.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zeitgeist-2.0)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  ruby-devel
BuildRequires:  vala
# /oreon:deps
%description
This package is a meta package for Cairo-Dock plugins.

%package	base
Summary:	Base files for Cairo-Dock plugins
Requires:	cairo-dock-core%{?_isa} >= %{core_least_ver}
Requires:	%{name}-common = %{version}-%{release}
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
%endif
%cmake_build
%install
%cmake_install
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
sed -i .%{_datadir}/cairo-dock/plug-ins/Dbus/CDApplet.h \
	-e '\@def@s|__.*\(DBUS_INTERFACES_VALA_SRC_CDAPPLET_H__\)|__\1|'
popd
%find_lang cairo-dock-plugins
%ldconfig_scriptlets -n cairo-dock-vala
%oreon_autofiles cairo-dock-plug-ins-base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-dbus usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-xfce usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-kde usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-webkit usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-plug-ins-unstable usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-python3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-ruby usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-vala usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-vala-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cairo-dock-plug-ins-base -f %{oreon_filedir}/cairo-dock-plug-ins-base.list
%files -n cairo-dock-plug-ins-common -f %{oreon_filedir}/cairo-dock-plug-ins-common.list
%files -n cairo-dock-plug-ins-dbus -f %{oreon_filedir}/cairo-dock-plug-ins-dbus.list
%files -n cairo-dock-plug-ins-xfce -f %{oreon_filedir}/cairo-dock-plug-ins-xfce.list
%files -n cairo-dock-plug-ins-kde -f %{oreon_filedir}/cairo-dock-plug-ins-kde.list
%files -n cairo-dock-plug-ins-webkit -f %{oreon_filedir}/cairo-dock-plug-ins-webkit.list
%files -n cairo-dock-plug-ins-unstable -f %{oreon_filedir}/cairo-dock-plug-ins-unstable.list
%files -n cairo-dock-python3 -f %{oreon_filedir}/cairo-dock-python3.list
%files -n cairo-dock-ruby -f %{oreon_filedir}/cairo-dock-ruby.list
%files -n cairo-dock-vala -f %{oreon_filedir}/cairo-dock-vala.list
%files -n cairo-dock-vala-devel -f %{oreon_filedir}/cairo-dock-vala-devel.list

%changelog

%autochangelog
