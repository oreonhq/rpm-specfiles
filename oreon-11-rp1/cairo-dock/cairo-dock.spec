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

##########################################
%global		flagrel	%{nil}
%global		use_gcc_strict_sanitize	0

%if	0%{?use_gcc_strict_sanitize} >= 1
%global		flagrel	%{flagrel}.san
%endif
##########################################

Name:			cairo-dock
Version:		%{mainver}%{?use_git:^%{gitdate}git%{shorthash}}
Release:		%{baserelease}%{?alphatag}%{?dist}%{flagrel}
Summary:		Light eye-candy fully themable animated dock

# Overall:		GPL-3.0-or-later
# data/scripts/cairo-dock-package-theme.sh	GPL-2.0-or-later
# src/gldit/gtk3imagemenuitem.c		LGPL-3.0-or-later
# SPDX confirmed
License:		GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later
URL:			http://glx-dock.org/
# Source0:		http://launchpad.net/cairo-dock-core/%%{urlver}/%%{mainver}/+download/cairo-dock-%%{mainver}.tar.gz
# Modified due to some may-be-patent-infringement issue
Source0:		cairo-dock-fedora-%{tarballver}.tar.gz
# Source0 is created by Source1
Source1:		cairo-dock-create-fedora-tarball.sh
# And some legal explanation
Source2:		LEGAL.fedora.cairo-dock
# https://github.com/Cairo-Dock/cairo-dock-core/pull/157
Patch0:		cairo-dock-pr157-disabled-zoom-feature.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  systemd-rpm-macros
%if 0%{?use_gcc_strict_sanitize}
BuildRequires:  libasan
BuildRequires:  libubsan
%endif

BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool

BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
#BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk-layer-shell-0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xtst)

Requires:	%{name}-core%{?isa} = %{version}-%{release}
Requires:	%{name}-plug-ins%{?isa} >= %{plugin_least_ver}
# Per upstream's request, install the below by default
Requires:	%{name}-plug-ins-xfce%{?isa} >= %{plugin_least_ver}
Requires:	%{name}-plug-ins-kde%{?isa} >= %{plugin_least_ver}

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
# Requires related to commands used internally
# in cairo-dock
Requires:	findutils
Requires:	curl
Requires:	xterm
# Ancient Obsoletes (and no provides)
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

# Currently -fPIE binary cannot work with ASAN on kernel 4.12
# https://github.com/google/sanitizers/issues/837
export CFLAGS="$(echo $CFLAGS     | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
export CXXFLAGS="$(echo $CXXFLAGS | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
export LDFLAGS="$(echo $LDFLAGS   | sed -e 's|-specs=[^ \t][^ \t]*hardened[^ \t][^ \t]*||g')"
%endif

# PATCH157 needs this: remove this when patch is included in tarball
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

## Desktop files
for f in $RPM_BUILD_ROOT%{_datadir}/applications/*desktop
do
	desktop-file-validate $f
done

%find_lang %{name}

# Cleanups
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/ChangeLog.txt

# Collect docment files
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

# Just to suppress rpmlint...
pushd $RPM_BUILD_ROOT
for f in \
	`find ./%{_datadir}/%{name} -name \*.desktop` \
	`find . -name \*.conf`
	do
		sed -i -e '1i\ ' $f
	done
popd

%ldconfig_scriptlets libs

%files

%files	libs
%license	licenses/*

%{_libdir}/libgldi.so.3*
%dir	%{_datadir}/%{name}/
%dir	%{_datadir}/%{name}/plug-ins/
%dir	%{_libdir}/%{name}/

%files	core -f %{name}.lang
%doc	documents/*

%{_bindir}/*%{name}*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/%{name}.svg

%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/*.desktop
%{_datadir}/%{name}/*.svg
%{_datadir}/%{name}/images/
%{_datadir}/%{name}/*view
#%%{_datadir}/%%{name}/emblems/
%{_datadir}/%{name}/explosion/
%{_datadir}/%{name}/gauges/
%{_datadir}/%{name}/icons/
%{_datadir}/%{name}/scripts/
%dir	%{_datadir}/%{name}/themes/

%{_datadir}/%{name}/themes/Default-Panel/
%{_datadir}/%{name}/themes/Default-Single/

%{_libdir}/%{name}/libcd-Help.so
%{_datadir}/%{name}/plug-ins/Help/

%{_userunitdir}/%{name}.service

%{_mandir}/man1/%{name}.1*

%files	devel
%{_includedir}/%{name}/
%{_libdir}/libgldi.so
%{_libdir}/pkgconfig/gldi.pc

%changelog
%autochangelog
