%global source0_hash 6ddc12a7b7eb32c1c11d634abfec61da50047df0bb999fa7edfaa799d1d214fa

Name:           appx-util
Version:        0.5
Release:        9%{?dist}
Summary:        Utility to create Microsoft .appx packages

# See LICENSING.md for details
License:        MPL-2.0 and BSD-3-Clause
URL:            https://github.com/OSInside/appx-util
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# For tests
%if 0%{?el8}
BuildRequires:  /usr/bin/python3.6
%else
BuildRequires:  /usr/bin/python3
%endif

%description
appx is a tool which creates and optionally signs
Microsoft Windows APPX packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE* LICENSING.md
%doc README.md CONTRIBUTING.md
%{_bindir}/appx

%changelog
%autochangelog
