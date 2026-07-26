%global source0_hash ea55d1641b4573b19103ca596368e418aecd2a1409adbdce3a9f76dc8ebad590

%define __cmake_in_source_build 1
Name:       ArpON
Version:    3.0
Release:    33%{?dist}
Summary:    ARP handler inspection

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://arpon.sourceforge.net/
Source0:    http://downloads.sourceforge.net/project/arpon/arpon/ArpON-%{version}/ArpON-%{version}-ng.tar.gz
Patch1:     ArpON-gcc-7-fixes.patch
Patch2:     ArpON-gcc-8-fixes.patch
Patch3:     ArpON-atu1.patch

BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  cmake
BuildRequires:  libnet-devel
BuildRequires:  libdnet-devel
BuildRequires: make

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

%files
%license LICENSE
%doc AUTHOR CHANGELOG doc/*
%{_sbindir}/arpon
/etc/arpon.conf
/var/log/arpon.log
%{_mandir}/man8/arpon.8*

%changelog
%autochangelog
