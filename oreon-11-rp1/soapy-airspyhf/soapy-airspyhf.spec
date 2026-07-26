%global source0_hash 1fad29401b6709fab78e408235211ab74f41bdab2f4e906ab51d029e2ddc0e43

%global gitdate 20251009
%global commit 7457d6972d97ea6808a2774a9439501308e4c688
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           soapy-airspyhf
Version:        0.2.0^%{gitdate}git%{shortcommit}
Release:        %autorelease
Summary:        SoapySDR module for AirspyHF hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyAirspyHF
Source:         https://github.com/pothosware/SoapyAirspyHF/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  SoapySDR-devel
BuildRequires:  airspyhf-devel

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

%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules*/libairspyhfSupport.so

%changelog
%autochangelog
