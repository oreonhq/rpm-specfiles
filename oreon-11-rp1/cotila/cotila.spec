%global source0_hash 898ebfdf562cd1a3622870e17a703b38559cf2c607b2d5f79e6b3a55563af619

%undefine __cmake_in_source_build

Name: cotila
Version: 1.2.1
Release: 15%{?dist}

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/calebzulawski/cotila
Summary: Compile Time Linear Algebra
Source0: %{url}/archive/%{version}.tar.gz
BuildArch: noarch

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gcc

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cotila-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md AUTHORS
%license LICENSE
%{_datadir}/cmake/%{name}/
%{_includedir}/%{name}/

%changelog
%autochangelog
