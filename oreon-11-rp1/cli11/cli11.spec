%global source0_hash 46eef3101da70852ec7af026e09d485ccee81813331c8c6052d39344443b83da
%global debug_package %{nil}
%global _docdir_fmt %{name}-devel
Name:           cli11
Version:        2.7.2
Release:        1%{?dist}
Summary:        Command line parser for C++11
License:        BSD-3-Clause
URL:            https://github.com/CLIUtils/CLI11
VCS:            git:%{url}.git
Source0:        https://github.com/CLIUtils/CLI11/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(catch2-with-main)
BuildRequires:  python3-devel
# /oreon:deps
%description
CLI11 is a command line parser for C++11 and beyond that provides a rich
feature set with a simple and intuitive interface.

%package devel
Summary:        Command line parser for C++11
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description devel
CLI11 is a command line parser for C++11 and beyond that provides a rich
feature set with a simple and intuitive interface.

%package        docs
License:        BSD-3-Clause AND GPL-1.0-or-later AND MIT
Summary:        Documentation for CLI11
BuildArch:      noarch
%description    docs
Documentation for CLI11.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CLI11-%{version}

%conf
# Alter the icon path in README.md for the installed paths
sed -i.orig 's,\./docs,.,' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build

CXXFLAGS='%{build_cxxflags} -DCLI11_OPTIONAL -DCLI11_STD_OPTIONAL=1'
%cmake \
    -DCLI11_BUILD_DOCS:BOOL=FALSE \
    -DCLI11_BUILD_TESTS:BOOL=TRUE \
    -DCMAKE_CXX_STANDARD=20
%cmake_build
%install
%cmake_install
%oreon_autofiles cli11-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cli11-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n cli11-devel -f %{oreon_filedir}/cli11-devel.list
%files -n cli11-docs -f %{oreon_filedir}/cli11-docs.list

%changelog

%autochangelog
