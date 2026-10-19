%global source0_hash 081c1fb5091cb8a1660ea9c152b689de9ba191d10a1109df503f5754f318af7e
%{?mingw_package_header}
Name: mingw-libgovirt
Version: 0.3.11
Release:        1%{?dist}
Summary:        MinGW support for a GObject library for interacting with oVirt REST API
License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/libgovirt
Source0:        http://download.gnome.org/sources/libgovirt/0.3/libgovirt-%{version}.tar.xz
Patch: 0001-build-sys-add-introspection-option.patch
BuildArch: noarch
Requires: pkgconfig
Requires: glib2-devel
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-rest
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-rest
BuildRequires:  ninja-build
# /oreon:deps
%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt
Summary:        MinGW support for a GObject library for interacting with oVirt REST API
%description -n mingw32-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt-static
Summary:        MinGW support for a GObject library for interacting with oVirt REST API
Requires:       mingw32-libgovirt = %{version}-%{release}
%description -n mingw32-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt
Summary:        MinGW support for a GObject library for interacting with oVirt REST API
%description -n mingw64-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt-static
Summary:        MinGW support for a GObject library for interacting with oVirt REST API
Requires:       mingw64-libgovirt = %{version}-%{release}
%description -n mingw64-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libgovirt-%{version}
%oreon_prep
%build

%mingw_meson --default-library=both -Dintrospection=disabled
%mingw_ninja
%install
%mingw_ninja_install
%mingw_find_lang libgovirt --all-name
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libgovirt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libgovirt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgovirt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgovirt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgovirt -f %{oreon_filedir}/mingw32-libgovirt.list
%files -n mingw32-libgovirt-static -f %{oreon_filedir}/mingw32-libgovirt-static.list
%files -n mingw64-libgovirt -f %{oreon_filedir}/mingw64-libgovirt.list
%files -n mingw64-libgovirt-static -f %{oreon_filedir}/mingw64-libgovirt-static.list

%changelog

%autochangelog
