%global source0_hash 757c3c3bd17c5a12c7168db2f2f0fd274457e65f35e23c5ec9aec34e3ef54ece

Name:           soapy-rtlsdr
Version:        0.3.3
Release:        2%{?dist}
Summary:        SoapySDR module for RTL-SDR hardware

License:        MIT
URL:            https://github.com/pothosware/SoapyRTLSDR
Source0:        https://github.com/pothosware/SoapyRTLSDR/archive/refs/tags/soapy-rtl-sdr-%{version}.tar.gz

BuildRequires:  cmake gcc-c++ SoapySDR-devel rtl-sdr-devel

%description
SoapyRTLSDR is a plug-in module for SoapySDR adding support for
RTL-SDR hardware.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SoapyRTLSDR-soapy-rtl-sdr-%{version}

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets
%files
%license LICENSE.txt
%{_libdir}/SoapySDR/modules*/librtlsdrSupport.so

%changelog
%autochangelog
