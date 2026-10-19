%global source0_hash 2e6dd3bed96479332c4c8e4cab2505699ade418a07797f64ee0d4fa394555032
%global forgeurl https://github.com/tevador/RandomX
Name:    randomx
Version: 1.2.1
Release:        1%{?dist}
Summary:        A proof-of-work algorithm that is optimized for general-purpose CPUs
License: BSD-3-Clause
URL:     %forgeurl
%forgemeta
Source0:        %{forgeurl}/archive/v%{version}/RandomX-%{version}.tar.gz
Patch0: randomx-sharedlib.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
# /oreon:deps
%description
RandomX is a proof-of-work (PoW) algorithm that is optimized for
general-purpose CPUs. RandomX uses random code execution (hence the name)
together with several memory-hard techniques to minimize the efficiency
advantage of specialized hardware.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: RandomX development files
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n randomx-devel -f %{oreon_filedir}/randomx-devel.list

%changelog

%autochangelog
