%global source0_hash b12fc3579f2d007e43fef1dcc0f4b3f8c1070c2fb6a3f58b23c53c766243217c

%{?mingw_package_header}

Name: mingw-libgovirt
Version: 0.3.9
Release: 1%{?dist}
Summary: MinGW support for a GObject library for interacting with oVirt REST API

License: LGPL-2.0-or-later
URL: https://gitlab.gnome.org/GNOME/libgovirt
Source: http://download.gnome.org/sources/libgovirt/0.3/libgovirt-%{version}.tar.xz
Patch: 0001-build-sys-add-introspection-option.patch

BuildArch: noarch

Requires: pkgconfig
Requires: glib2-devel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: glib2-devel
BuildRequires: intltool
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-rest >= 0.7.92
BuildRequires: mingw64-rest >= 0.7.92

%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt
Summary:        %{summary}

%description -n mingw32-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw32-libgovirt-static
Summary:        %{summary}
Requires:       mingw32-libgovirt = %{version}-%{release}

%description -n mingw32-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt
Summary:        %{summary}

%description -n mingw64-libgovirt
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package -n     mingw64-libgovirt-static
Summary:        %{summary}
Requires:       mingw64-libgovirt = %{version}-%{release}

%description -n mingw64-libgovirt-static
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libgovirt-%{version}

%build
%mingw_meson --default-library=both -Dintrospection=disabled

%mingw_ninja

%install
%mingw_ninja_install

%mingw_find_lang libgovirt --all-name

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-libgovirt -f mingw32-libgovirt.lang
%doc AUTHORS COPYING MAINTAINERS README
%{mingw32_bindir}/libgovirt-2.dll
%{mingw32_libdir}/libgovirt.dll.a
%{mingw32_libdir}/pkgconfig/govirt-1.0.pc
%dir %{mingw32_includedir}/govirt-1.0/
%dir %{mingw32_includedir}/govirt-1.0/govirt/
%{mingw32_includedir}/govirt-1.0/govirt/*.h

%files -n mingw32-libgovirt-static
%{mingw32_libdir}/libgovirt.a

%files -n mingw64-libgovirt -f mingw64-libgovirt.lang
%doc AUTHORS COPYING MAINTAINERS README
%{mingw64_bindir}/libgovirt-2.dll
%{mingw64_libdir}/libgovirt.dll.a
%{mingw64_libdir}/pkgconfig/govirt-1.0.pc
%dir %{mingw64_includedir}/govirt-1.0/
%dir %{mingw64_includedir}/govirt-1.0/govirt/
%{mingw64_includedir}/govirt-1.0/govirt/*.h

%files -n mingw64-libgovirt-static
%{mingw64_libdir}/libgovirt.a

%changelog
%autochangelog
