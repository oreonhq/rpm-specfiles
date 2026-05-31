%global source0_hash 43d3436c0199496ee18aca4f875fe3926a40a0fae781bc280cdb96f7b5068ac0

# the package gets input from scanner devices from network
# can be possibly dangerous if an attacker camouflages himself
# as a scanner
%global _hardened_build 1

Name:           sane-airscan
Version:        0.99.36
Release:        2%{?dist}
Summary:        SANE backend for AirScan (eSCL) and WSD document scanners
# SANE related source and header files - GPL 2.0+ with SANE exception
# http_parser.c/.h - MIT
# the exception is defined in LICENSE, meant for SANE project in most cases
License:        GPL-2.0-or-later WITH SANE-exception AND MIT
URL:            https://github.com/alexpevzner/sane-airscan
Source:        https://github.com/alexpevzner/sane-airscan/archive/0.99.36/sane-airscan-0.99.36.tar.gz

# backported from upstream


# needed for querying and getting mDNS messages from local network
BuildRequires:  avahi-devel
# project is written in C
BuildRequires:  gcc
# fuzzer for testing is written in C++
BuildRequires:  gcc-c++
# git is used during autosetup
BuildRequires:  git-core
# creating credentials and SHA256 for UUID
BuildRequires:  gnutls-devel
# needed for creating output image
BuildRequires:  libjpeg-turbo-devel, libpng-devel
# XML data are carried on HTTP protocol, we need to create them and parse them
BuildRequires:  libxml2-devel
# uses meson
BuildRequires: meson
# used in Makefile to get the correct compile and link flags
BuildRequires:  pkgconf-pkg-config
# package is meant to be as one of SANE backends - it uses SANE API for handling
# devices, strings, words (bytes) and backend itself
BuildRequires:  sane-backends-devel

%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9
Recommends: ipp-usb
%endif

# needs shared library implementing the backend
Requires: libsane-airscan%{?_isa} = %{version}-%{release}

%description
This package contains a tool for discovering scanning devices in cases
when automatic discovery fails - airscan-discover.

%package -n libsane-airscan
Summary: SANE backend for eSCL or WSD

# USB scanners which support IPP-over-USB interface can communicate
# via sane-airscan once ipp-usb brings up an IPP interface for them
# remove for now until migration app is implemented
#Recommends: ipp-usb

%description -n libsane-airscan
This package contain a SANE backend for MFP and document scanners that
implements either eSCL (AirScan/AirPrint scanning) or WSD "driverless"
scanning protocol.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

rm -f %{buildroot}%{_libdir}/sane/libsane-airscan.so

%files
%license COPYING LICENSE
%{_bindir}/airscan-discover
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man1/airscan-discover.1*

%files -n libsane-airscan
%license COPYING LICENSE
%dir %{_sysconfdir}/sane.d
%config(noreplace) %{_sysconfdir}/sane.d/airscan.conf
%dir %{_sysconfdir}/sane.d/dll.d
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/airscan
%dir %{_libdir}/sane
%{_libdir}/sane/libsane-airscan.so.1
# I'm not fond of wildcards in %%files, but FPG demands it for manpages
%{_mandir}/man5/sane-airscan.5*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.99.36-2
- Prepare for Oreon 11 (RP1)
