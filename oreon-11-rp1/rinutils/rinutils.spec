%global source0_hash f9e527d37a6cc8c7b8870ada63caa24f32ab0d29fd1116df3ebb686583030955
%define debug_package %{nil}
%global basen rinutils
Name: %{basen}
Version: 0.10.3
%global basenver %{basen}-%{version}
Release:        1%{?dist}
License: MIT
Source0:        https://github.com/shlomif/%{name}/releases/download/%{version}/%{basenver}.tar.xz
URL: https://github.com/shlomif/rinutils/
Summary:        Shlomi Fish's gnu11 C Library of Random headers
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  perl-devel
BuildRequires:  python3
# /oreon:deps
%description
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%package devel
Summary: Shlomi Fish's gnu11 C Library of Random headers (development package)
Provides: %{basen}-static = %{version}-%{release}
%description devel
Shlomi Fish's -std=gnu11 ( GCC / clang ) C library of random headers. Possibly
of limited general interest, but nevertheless free and open source software
(FOSS) under the MIT/Expat license.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{basenver}

%build

%cmake -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir} -DWITH_TEST_SUITE=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rinutils-devel -f %{oreon_filedir}/rinutils-devel.list

%changelog

%autochangelog
