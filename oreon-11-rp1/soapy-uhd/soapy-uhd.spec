%global source0_hash 9779cce2e732cd41905b6cf8ea85edbbf51b1ac918e6180bd4891eebb4c8d085
Name:		soapy-uhd
Version:	0.4.1
Release:        23%{?dist}
Summary:        Soapy SDR plugins for UHD supported SDR devices
License:	GPL-3.0-only
URL:		https://github.com/pothosware/SoapyUHD
Source0:        https://github.com/pothosware/SoapyUHD/archive/%{name}-%{version}.tar.gz
Requires:	uhd
Requires:	SoapySDR
Patch:		soapy-uhd-0.4.1-uhd-4.8-fix.patch
Patch:		soapy-uhd-cmake4-fix.patch
# oreon:deps
BuildRequires:  SoapySDR-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  uhd-devel
# /oreon:deps
%description
Soapy SDR plugins for UHD supported SDR devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir SoapyUHD-%{name}-%{version}
%oreon_prep
%build

%cmake \
%if "%{?_lib}"=="lib64"
  -DLIB_SUFFIX=64
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
