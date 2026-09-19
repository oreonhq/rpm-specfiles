%global source0_hash f9e527d37a6cc8c7b8870ada63caa24f32ab0d29fd1116df3ebb686583030955

%define debug_package %{nil}
%global basen rinutils

Name: %{basen}
Version: 0.10.3
%global basenver %{basen}-%{version}
Release: 5%{dist}
License: MIT
Source:  https://github.com/shlomif/rinutils/releases/download/%{version}/%{basenver}.tar.xz
URL: https://github.com/shlomif/rinutils/
Summary: Shlomi Fish's gnu11 C Library of Random headers
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: glibc-devel
BuildRequires: perl-devel
BuildRequires: python3

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

%files devel
%license LICENSE
%doc README.asciidoc NEWS.asciidoc
%{_includedir}/%{basen}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/Rinutils/*.cmake

%changelog
%autochangelog
