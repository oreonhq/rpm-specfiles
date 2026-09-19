%global source0_hash 9779cce2e732cd41905b6cf8ea85edbbf51b1ac918e6180bd4891eebb4c8d085

Name:		soapy-uhd
Version:	0.4.1
Release:	23%{?dist}
Summary:	Soapy SDR plugins for UHD supported SDR devices
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/pothosware/SoapyUHD
Source:		%{URL}/archive/%{name}-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	uhd-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	boost-devel
# For module directories
Requires:	uhd
Requires:	SoapySDR
# https://github.com/pothosware/SoapyUHD/commit/6b521393cc45c66770f3d4bc69eac7dda982174c.patch
Patch:		soapy-uhd-0.4.1-uhd-4.8-fix.patch
# Already in upstream
Patch:		soapy-uhd-cmake4-fix.patch

%description
Soapy SDR plugins for UHD supported SDR devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SoapyUHD-%{name}-%{version}

%build
# LIB_SUFFIX workaround for https://github.com/pothosware/SoapyUHD/commit/6b521393cc45c66770f3d4bc69eac7dda982174c.patch
# https://github.com/pothosware/SoapyUHD/issues/62
%cmake \
%if "%{?_lib}"=="lib64"
  -DLIB_SUFFIX=64
%endif

%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md Changelog.txt
%{_libdir}/SoapySDR/modules*.*/*.so
%{_libdir}/uhd/modules/*.so

%changelog
%autochangelog
