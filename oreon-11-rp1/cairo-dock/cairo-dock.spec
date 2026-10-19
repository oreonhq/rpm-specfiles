%global source0_hash dcd18340a954d7ea550531087d0b2af0b60b9b9619ff6f5b1e010af3cf0d8fce
%global	urlver	3.6
%global	mainver	3.6.2
%global	plugin_least_ver	3.6.0
%dnl %global	use_git	1
%global	gitdate	20250922
%global	githash	bbdf30b67241dbf61dea651b636a07da5cc39049
%global	shorthash	%(c=%{githash} ; echo ${c:0:7})
%global	tarballver	%{mainver}%{?use_git:-%{gitdate}git%{shorthash}}
%global	baserelease	3
%dnl %global	alphatag		.rcb
%undefine _ld_strict_symbol_defs
%undefine __brp_mangle_shebangs
%global		flagrel	%{nil}
%global		use_gcc_strict_sanitize	0
%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
Name:			cairo-dock
Version:		%{mainver}%{?use_git:^%{gitdate}git%{shorthash}}
Release:        3%{?dist}
Summary:        Light eye-candy fully themable animated dock
License:		GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later
URL:			http://glx-dock.org/
Source0:        %{name}-fedora-%{version}.tar.gz
Source1:		cairo-dock-create-fedora-tarball.sh
Source2:		LEGAL.fedora.cairo-dock
Patch0:		cairo-dock-pr157-disabled-zoom-feature.patch
%if 0%{?use_gcc_strict_sanitize}
%endif
Requires:	%{name}-core%{?isa} = %{version}-%{release}
Requires:	%{name}-plug-ins%{?isa} >= %{plugin_least_ver}
Requires:	%{name}-plug-ins-xfce%{?isa} >= %{plugin_least_ver}
Requires:	%{name}-plug-ins-kde%{?isa} >= %{plugin_least_ver}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
This is a metapackage for installing all default packages
related to cairo-dock.

%package	libs
Summary:	Library files for %{name}
%description	libs
This package contains library files for %{name}.

%package	core
Summary:	Core files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	findutils
Requires:	curl
Requires:	xterm
Obsoletes:	%{name}-plug-ins-gecko < %{version}-%{release}
Obsoletes:	%{name}-themes < %{version}-%{release}
%description	core
An light eye-candy fully themable animated dock for any 
Linux desktop. It has a family-likeness with OSX dock,
but with more options.

This is the core package of cairo-dock.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries, build data, and header
files for developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{mainver}%{?use_git:-%{gitdate}git%{shorthash}} -p1

## permission
# %%_fixperms cannot fix permissions completely here
for dir in */
do
	find $dir -type f | xargs -r chmod 0644
done
chmod 0644 [A-Z]*
chmod 0755 */

# cmake issue
sed -i.debuglevel \
	-e '\@add_definitions@s|-O3|-O2|' \
	CMakeLists.txt
sed -i.stat \
	-e 's|\${MSGFMT_EXECUTABLE}|\${MSGFMT_EXECUTABLE} --statistics|' \
	po/CMakeLists.txt

# Modify version forcely
%if 0%{?use_git}
sed -i CMakeLists.txt -e '\@set (VERSION @s|VERSION.*|VERSION "%{mainver}")|'
%endif

# Don't set rpath
sed -i CMakeLists.txt -e '\@APPEND.*CMAKE_INSTALL_RPATH@d'

# Don't check / try systemd-notify on buildroot
sed -i CMakeLists.txt -e '\@SYSTEMD_COMMAND@s|systemd-notify|true|'

%build

%set_build_flags
%if 0%{?use_gcc_strict_sanitize}
export CC="${CC} -fsanitize=address -fsanitize=undefined"
export CXX="${CXX} -fsanitize=address -fsanitize=undefined"
export LDFLAGS="${LDFLAGS} -pthread"
export CFLAGS="$(echo $CFLAGS     | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
export CXXFLAGS="$(echo $CXXFLAGS | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
export LDFLAGS="$(echo $LDFLAGS   | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
%endif
export CFLAGS="$CFLAGS -DAVOID_PATENT_CRAP=1"
rm -f CMakeCache.txt
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-Denable-egl-support:BOOL=ON \
	%{nil}
%cmake_build
%install
%cmake_install
chmod 0755 ${RPM_BUILD_ROOT}%{_libdir}/lib*.so.*
for f in $RPM_BUILD_ROOT%{_datadir}/applications/*desktop
do
	desktop-file-validate $f
done
%find_lang %{name}
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/ChangeLog.txt
rm -rf documents licenses
mkdir documents licenses
install -cpm 644 \
	ChangeLog \
	data/ChangeLog*.txt \
	documents/
install -cpm 644 \
	LGPL-2 \
	LICENSE \
	copyright \
	%{SOURCE2} \
	licenses/
pushd $RPM_BUILD_ROOT
for f in \
	`find ./%{_datadir}/%{name} -name \*.desktop` \
	`find . -name \*.conf`
	do
		sed -i -e '1i\ ' $f
	done
popd
%ldconfig_scriptlets libs
%oreon_autofiles cairo-dock-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-core usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-dock-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cairo-dock-libs -f %{oreon_filedir}/cairo-dock-libs.list
%files -n cairo-dock-core -f %{oreon_filedir}/cairo-dock-core.list
%files -n cairo-dock-devel -f %{oreon_filedir}/cairo-dock-devel.list

%changelog

%autochangelog
