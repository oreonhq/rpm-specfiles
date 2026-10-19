%global source0_hash bb4681f9bfb9cc175cf2c2afbf55706975db45d55d11701f52cb4e436377ae0b
%define			debug_package %{nil}
Name:			ndesk-dbus
Version:		0.6.1a
Release:        1%{?dist}
Summary:        Managed C# implementation of DBus
License:		MIT
URL:			http://www.ndesk.org/DBusSharp
Source0:        http://www.ndesk.org/archive/dbus-sharp/ndesk-dbus-%{version}.tar.gz
Patch0:			%{name}-sugar-datastore.patch
Requires:		mono-core
ExclusiveArch:          %{mono_arches}
# oreon:deps
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%description
Managed C# implementation of DBus

%package devel
Summary:		Develpment files for the managed C# implementation of DBus
Requires:		%{name} = %{version}-%{release}
Requires:		pkgconfig
%description devel
Development files for ndesk-dbus

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .sugar-datastore

sed -i "s#gmcs#mcs#g" configure
sed -i "s#gmcs#mcs#g" configure.ac

%build

%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT%{_prefix}/lib/pkgconfig/*.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ndesk-dbus-devel -f %{oreon_filedir}/ndesk-dbus-devel.list

%changelog

%autochangelog
