%global source0_hash 0a6d5fe7be55b6301615d71b89507b712f287b4ba498b798301333ffabe06769
%define			debug_package %{nil}
Name:			ndesk-dbus-glib
URL:			http://www.ndesk.org/DBusSharp
License:		MIT
Version:		0.4.1
Release:        1%{?dist}
Summary:        Provides glib mainloop integration for ndesk-dbus
Source0:        http://www.ndesk.org/archive/dbus-sharp/ndesk-dbus-glib-%{version}.tar.gz
ExclusiveArch:	%{mono_arches}
# oreon:deps
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  ndesk-dbus-devel
# /oreon:deps
%description
ndesk-dbus-glib provides glib mainloop integration for ndesk-dbus

%package devel
Summary:		Development files for ndesk-dbus-glib
Requires:		ndesk-dbus-glib = %{version}
Requires:		ndesk-dbus-devel
Requires:		pkgconfig
%description devel
Development files for ndesk-dbus-glib

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build

%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ndesk-dbus-glib-devel -f %{oreon_filedir}/ndesk-dbus-glib-devel.list

%changelog

%autochangelog
