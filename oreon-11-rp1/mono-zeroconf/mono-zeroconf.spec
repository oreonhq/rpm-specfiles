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
# Combination of:
# https://github.com/mono/Mono.Zeroconf/commit/f71474ddfae108d500e1c72fba64c50be77822a5
# https://github.com/JvetS/Mono.Zeroconf/commit/7d4a254191e0494dd2ba3ebc008f7ff20b11fe97
Patch1:		mono-zeroconf-0.9.0-fix-host-byte-order-bug.patch
# https://github.com/mono/Mono.Zeroconf/commit/e6700384f850085b93b358118521c991f6c1ae31
Patch2:		mono-zeroconf-0.9.0-async-prefix.patch
# https://github.com/mono/Mono.Zeroconf/commit/72a9cd4329661d2d03fa6934690ab20270d8912b
Patch3:		mono-zeroconf-0.9.0-correct-service-type-for-DNSServiceQueryRecord.patch
# https://github.com/mono/Mono.Zeroconf/pull/12
Patch4:		mono-zeroconf-0.9.0-ipv6-fixes.patch
# https://github.com/mono/Mono.Zeroconf/pull/11
Patch5:		mono-zeroconf-0.9.0-fix-unreliable-browse-resolve.patch
# https://github.com/mono/Mono.Zeroconf/pull/6
Patch6:		mono-zeroconf-0.9.0-fix-recursive-dispose.patch
# https://github.com/mono/Mono.Zeroconf/pull/7
Patch7:		mono-zeroconf-0.9.0-name-collision-fix.patch
# https://github.com/mono/Mono.Zeroconf/pull/9
Patch8:		mono-zeroconf-0.9.0-utf8-service-names.patch
# https://github.com/mono/Mono.Zeroconf/pull/10
Patch9:		mono-zeroconf-0.9.0-set-host-target.patch
# Fix NDesk.DBus to be just DBus
Patch10:	mono-zeroconf-0.9.0-dbus-fix.patch
# Proper libnss_mdns
Patch11:	mono-zeroconf-0.9.0-proper-libnss_mdns.patch
BuildRequires: make
BuildRequires:  mono-devel monodoc-devel dbus-sharp-devel
Requires:       mono-core dbus-sharp nss-mdns

# Mono only available on these:
ExclusiveArch: %mono_arches

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
#parallel build doesn't work
make

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files 
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mzclient
%{_prefix}/lib/mono-zeroconf/
%{_prefix}/lib/mono/gac/Mono.Zeroconf
%{_prefix}/lib/mono/mono-zeroconf
%{_prefix}/lib/mono/gac/policy.*

%files devel
%{_libdir}/pkgconfig/mono-zeroconf.pc

%changelog
%autochangelog
