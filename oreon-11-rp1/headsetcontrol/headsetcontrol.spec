%global source0_hash 63bfd147c82277bfcf2314ad2b01ca4e4bf06e1d5516e01ee39232661f4d5144

Name:           headsetcontrol
Version:        3.0.0
Release:        6%{?dist}
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
# The entire source code is GPLv3+ except cmake_modules/Findhidapi.cmake which is Boost
# Automatically converted from old format: GPLv3+ and Boost - review is highly recommended.
License:        GPL-3.0-or-later AND BSL-1.0 
URL:            https://github.com/Sapd/HeadsetControl
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         3.0.0_build_fix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  hidapi-devel

%description
A tool to control certain aspects of USB-connected headsets on Linux

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HeadsetControl-%{version}
%patch -P0 -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{_bindir}/headsetcontrol
%{_prefix}/lib/udev/rules.d/70-headsets.rules
%license license
%doc README.md

%changelog
%autochangelog
