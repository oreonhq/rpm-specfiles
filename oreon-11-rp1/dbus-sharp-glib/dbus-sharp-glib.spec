%global source0_hash d5b44d3ffa419730df0a6a6fff1e6912c80bc364e4176444e48264853989ce3b

%define debug_package %{nil}

Summary: C# bindings for D-Bus glib main loop integration
Name: dbus-sharp-glib
Version: 0.6.0
Release: 23%{?dist}
URL: http://mono.github.com/dbus-sharp/
Source0: https://github.com/mono/dbus-sharp-glib/releases/download/v0.6/%{name}-%{version}.tar.gz
License: MIT
BuildRequires: mono-devel
BuildRequires: dbus-sharp-devel >= 1:0.8.0
BuildRequires: make
# Mono only available on these:
ExclusiveArch: %mono_arches

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

%files
%doc COPYING README
%{_prefix}/lib/mono/dbus-sharp-glib-2.0
%{_prefix}/lib/mono/gac/dbus-sharp-glib

%files devel
%{_libdir}/pkgconfig/dbus-sharp-glib-2.0.pc

%changelog
%autochangelog
