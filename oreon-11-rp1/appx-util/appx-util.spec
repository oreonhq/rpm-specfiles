%global source0_hash 6ddc12a7b7eb32c1c11d634abfec61da50047df0bb999fa7edfaa799d1d214fa
Name:           appx-util
Version:        0.5
Release:        1%{?dist}
Summary:        Utility to create Microsoft .appx packages
License:        MPL-2.0 and BSD-3-Clause
URL:            https://github.com/OSInside/appx-util
Source0:        https://github.com/OSInside/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?el8}
%else
%endif
# oreon:deps
BuildRequires:  /usr/bin/python3
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
appx is a tool which creates and optionally signs
Microsoft Windows APPX packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
