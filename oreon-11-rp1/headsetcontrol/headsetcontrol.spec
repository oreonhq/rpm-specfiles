%global source0_hash 4009882eb97406a58d7a0665d3a21903641fa9dca0e70d73b8b708786fd60386
Name:           headsetcontrol
Version:        4.1.0
Release:        1%{?dist}
Summary:        A tool to control certain aspects of USB-connected headsets on Linux
License:        GPL-3.0-or-later AND BSL-1.0 
URL:            https://github.com/Sapd/HeadsetControl
Source0:        https://github.com/Sapd/HeadsetControl/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         4.1.0_build_fix.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hidapi-devel
# /oreon:deps
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
%oreon_autofiles main

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
