%global source0_hash 1e5b3b8373141caa37bf42fe74ae1950de3ff15c84966d8a415485d334ba5507
%global _hardened_build 1
Name:           sane-airscan
Version:        0.99.38
Release:        1%{?dist}
Summary:        SANE backend for AirScan (eSCL) and WSD document scanners
License:        GPL-2.0-or-later WITH SANE-exception AND MIT
URL:            https://github.com/alexpevzner/sane-airscan
Source0:        https://github.com/alexpevzner/sane-airscan/archive/refs/tags/0.99.38.tar.gz#/sane-airscan-0.99.36.tar.gz
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
Recommends: ipp-usb
%endif
Requires: libsane-airscan%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  avahi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gnutls-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  pkgconf-pkg-config
BuildRequires:  sane-backends-devel
# /oreon:deps
%description
This package contains a tool for discovering scanning devices in cases
when automatic discovery fails - airscan-discover.

%package -n libsane-airscan
Summary: SANE backend for eSCL or WSD
%description -n libsane-airscan
This package contain a SANE backend for MFP and document scanners that
implements either eSCL (AirScan/AirPrint scanning) or WSD "driverless"
scanning protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%check

%meson_test
%install
%meson_install
rm -f %{buildroot}%{_libdir}/sane/libsane-airscan.so
%oreon_autofiles libsane-airscan usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libsane-airscan -f %{oreon_filedir}/libsane-airscan.list

%changelog

%autochangelog
