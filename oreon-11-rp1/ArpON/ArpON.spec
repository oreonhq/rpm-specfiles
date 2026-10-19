%global source0_hash 0ca9eef2121518655243e3fcd5fad72ee2ee63a4ebaf352c78a39c41ccce9200
%define __cmake_in_source_build 1
Name:       ArpON
Version:    3.0
Release:        33%{?dist}
Summary:        ARP handler inspection
License:    LicenseRef-Callaway-BSD
URL:        http://arpon.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/arpon/arpon/ArpON-%{version}/ArpON-%{version}-ng.tar.gz
Patch1:     ArpON-gcc-7-fixes.patch
Patch2:     ArpON-gcc-8-fixes.patch
Patch3:     ArpON-atu1.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libdnet-devel
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
# /oreon:deps
%description
ArpON (ARP handler inspection) is a Host-based solution that make the ARP
standardized protocol secure in order to avoid the Man In The Middle (MITM)
attack through the ARP spoofing, ARP cache poisoning or ARP poison routing
attack.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-ng
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build

%cmake -DCMAKE_INSTALL_PREFIX="/" .
%{__make} %{?_smp_mflags}
%install
%{__install} -D -pm 755 src/arpon %{buildroot}%{_sbindir}/arpon
%{__install} -D -pm 644 man8/arpon.8 %{buildroot}%{_mandir}/man8/arpon.8
%{__install} -D -pm 644 etc/arpon.conf %{buildroot}/etc/arpon.conf
%{__install} -D -pm 644 log/arpon.log %{buildroot}/var/log/arpon.log
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
