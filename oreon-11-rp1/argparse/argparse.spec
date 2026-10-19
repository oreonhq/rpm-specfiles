%global source0_hash 9dcb3d8ce0a41b2a48ac8baa54b51a9f1b6a2c52dd374e28cc713bab0568ec98
%global debug_package %{nil}
Name:           argparse
Version:        3.2
Release:        1%{?dist}
Summary:        Argument parser for modern C++
ExcludeArch:    %{ix86}
License:        MIT
URL:            https://github.com/p-ranav/argparse
VCS:            git:%{url}.git
Source0:        https://github.com/p-ranav/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
Argparse is an argument parser for C++17 in a single header file.

%package devel
Summary:        Argument parser for modern C++
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description devel
Argparse is an argument parser for C++17 in a single header file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%conf
# Install into the noarch directory
# https://github.com/p-ranav/argparse/pull/323
sed -i 's/CMAKE_INSTALL_LIBDIR/CMAKE_INSTALL_DATADIR/' CMakeLists.txt

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles argparse-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{_vpath_builddir}/test/tests
%files -f %{oreon_filedir}/main.list
%files -n argparse-devel -f %{oreon_filedir}/argparse-devel.list

%changelog

%autochangelog
