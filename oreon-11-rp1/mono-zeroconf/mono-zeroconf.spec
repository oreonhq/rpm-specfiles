%global source0_hash 6bde77b0240a45b148f182677022cf20d8ee8e1711b220a1162c9fae3726d7e1
%define         debug_package %{nil}
Name:           mono-zeroconf
Version:        0.9.0
Release:        42%{?dist}
Summary:        Mono.Zeroconf networking library
License:        MIT
URL:            http://banshee-project.org/files/mono-zeroconf
Source0:        %{name}-%{version}.tar.bz2
Patch0:		mono-zeroconf-0.9.0-use-system-ndesk-dbus.patch
Patch1:		mono-zeroconf-0.9.0-fix-host-byte-order-bug.patch
Patch2:		mono-zeroconf-0.9.0-async-prefix.patch
Patch3:		mono-zeroconf-0.9.0-correct-service-type-for-DNSServiceQueryRecord.patch
Patch4:		mono-zeroconf-0.9.0-ipv6-fixes.patch
Patch5:		mono-zeroconf-0.9.0-fix-unreliable-browse-resolve.patch
Patch6:		mono-zeroconf-0.9.0-fix-recursive-dispose.patch
Patch7:		mono-zeroconf-0.9.0-name-collision-fix.patch
Patch8:		mono-zeroconf-0.9.0-utf8-service-names.patch
Patch9:		mono-zeroconf-0.9.0-set-host-target.patch
Patch10:	mono-zeroconf-0.9.0-dbus-fix.patch
Patch11:	mono-zeroconf-0.9.0-proper-libnss_mdns.patch
Requires:       mono-core dbus-sharp nss-mdns
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  dbus-sharp-devel
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  monodoc-devel
# /oreon:deps
%description
Mono.Zeroconf is a cross platform Zero Configuration Networking library
for Mono and .NET.

%package devel
Summary: Development files for Mono.Zeroconf
Requires: %{name} = %{version}-%{release} pkgconfig monodoc
%description devel
Development files and documentation for Mono.Zeroconf

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .system-dbus
%patch -P1 -p1 -b .hostbyteordere
%patch -P2 -p1 -b .prefix
%patch -P3 -p1 -b .dnsfix
%patch -P4 -p1 -b .ipv6fix
%patch -P5 -p1 -b .unreliable
%patch -P6 -p1 -b .recursivedispose
%patch -P7 -p1 -b .namecollision
%patch -P8 -p1 -b .utf8
%patch -P9 -p1 -b .hosttarget
%patch -P10 -p1 -b .dbusfix
%patch -P11 -p1 -b .2017
sed -i "s#gmcs#mcs#g" configure
sed -i "s#2.0#4.5#g" configure

%build

%configure --libdir=%{_prefix}/lib --disable-docs
make
%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-zeroconf-devel -f %{oreon_filedir}/mono-zeroconf-devel.list

%changelog

%autochangelog
