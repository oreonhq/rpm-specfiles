%global source0_hash bc11ac297b3cb010be904c72789695543ee3fdf3d75cdc8225fd371385af4e61

%bcond_without ecore

Name:          dbus-c++
Version:       0.9.0
Release:       38%{?dist}
Summary:       Native C++ bindings for D-Bus

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://sourceforge.net/projects/dbus-cplusplus/
Source0:        http://downloads.sourceforge.net/dbus-cplusplus/libdbus-c++-0.9.0.tar.gz

Patch1: dbus-c++-gcc4.7.patch
Patch2: dbus-c++-linkfix.patch
# Fix collision between macro bind_property in dbus-c++/interface.h and method
# bind_property in glibmm/binding.h
Patch3: dbus-c++-macro_collision.patch
# Remove broken classes for multithreading support
# https://sourceforge.net/p/dbus-cplusplus/patches/18/
Patch4: dbus-c++-threading.patch
# https://sourceforge.net/p/dbus-cplusplus/patches/19/
Patch5: dbus-c++-writechar.patch
# Fix template/operator issues
# https://github.com/pkgw/dbus-cplusplus/commit/a0b9ef3b469ca23c6a3229d8abb967cbbddcee38
Patch6: dbus-c++-template-operators.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires: dbus-devel
BuildRequires: glib2-devel
BuildRequires: gtkmm24-devel
BuildRequires: autoconf automake libtool
BuildRequires: expat-devel
%if %{with ecore}
BuildRequires: ecore-devel
%endif
BuildRequires: make

%description
dbus-c++ attempts to provide a C++ API for D-Bus.
Subpackages are provided with mainloop integration.

%if %{with ecore}
%package       ecore
Summary:       Ecore library for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   ecore
This package contains the ecore mainloop library for %{name}
%endif

%package       glib
Summary:       GLib library for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   glib
This package contains the GLib mainloop library for %{name}

%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      pkgconfig
%description   devel
This package contains libraries and header files for
developing applications that use %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n lib%{name}-%{version}
sed -i 's/\r//' AUTHORS
sed -i 's/libtoolize --force --copy/libtoolize -if --copy/' bootstrap
%patch -P1 -p1 -b .gcc47
%patch -P2 -p1 -b .linkfix
%patch -P3 -p1 -b .collision
%patch -P4 -p1 -b .threading
%patch -P5 -p1 -b .writechar
%patch -P6 -p1 -b .template-operators

%build
autoreconf -vfi
export CPPFLAGS='%{optflags}' CXXFLAGS='--std=gnu++11 %{optflags}'
%configure --disable-static --disable-tests \
%if %{without ecore}
           --disable-ecore
%else
  ;
%endif
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -print -delete

%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS
%{_bindir}/dbusxx-introspect
%{_bindir}/dbusxx-xml2cpp
%{_libdir}/libdbus-c++-1.so.0*

%if %{with ecore}
%files ecore
%{_libdir}/libdbus-c++-ecore-1.so.0*
%endif

%files glib
%{_libdir}/libdbus-c++-glib-1.so.0*

%files devel
%doc TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.0-38
- Prepare for Oreon 11 (RP1)
