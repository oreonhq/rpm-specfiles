%global source0_hash d5b44d3ffa419730df0a6a6fff1e6912c80bc364e4176444e48264853989ce3b
%define debug_package %{nil}
Summary:        C# bindings for D-Bus glib main loop integration
Name: dbus-sharp-glib
Version: 0.6.0
Release:        1%{?dist}
URL: http://mono.github.com/dbus-sharp/
Source0:        https://github.com/mono/dbus-sharp-glib/releases/download/v0.6/%{name}-%{version}.tar.gz
License: MIT
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  dbus-sharp-devel
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%description
C# bindings for D-Bus glib main loop integration

%package devel
Summary: Development files for D-Bus Sharp
Requires: %name = %{version}-%{release}
Requires: pkgconfig
%description devel
Development files for D-Bus Sharp development.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build

export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure --libdir=%{_prefix}/lib
make
%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
%oreon_autofiles dbus-sharp-glib-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n dbus-sharp-glib-devel -f %{oreon_filedir}/dbus-sharp-glib-devel.list

%changelog

%autochangelog
