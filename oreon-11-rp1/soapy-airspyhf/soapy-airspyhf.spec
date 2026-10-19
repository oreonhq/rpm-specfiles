%global source0_hash 1fad29401b6709fab78e408235211ab74f41bdab2f4e906ab51d029e2ddc0e43
%global gitdate 20251009
%global commit 7457d6972d97ea6808a2774a9439501308e4c688
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           soapy-airspyhf
Version:        0.2.0^%{gitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        SoapySDR module for AirspyHF hardware
License:        MIT
URL:            https://github.com/pothosware/SoapyAirspyHF
Source0:        https://github.com/pothosware/SoapyAirspyHF/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyhf-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
SoapyAirspyHF is a plug-in module for SoapySDR adding support for
AispyHF hardware.
    
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SoapyAirspyHF-%{commit}

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
