# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 42c36e1ef1307b1186996e4644f9999970e26325670b99019f3408bf0d3c952a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build
%global debug_package %{nil}
%global ftest_commit c4ad4af0946b73ce1a40cbc72205d15d196c7e06
%global ftest_shortcommit %(c=%{ftest_commit}; echo ${c:0:7})

Name:       utf8cpp
Version:    5.0.0
Release:    1%{?dist}
Summary:    A simple, portable and lightweight library for handling UTF-8 encoded strings
License:    BSL-1.0
URL:        https://github.com/nemtrif/utfcpp
Source0:    https://github.com/nemtrif/utfcpp/archive/v%{version}/utfcpp-%{version}.tar.gz
Patch0:     %{name}-cmake.patch
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: cmake
%description
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package    devel
Summary:    Header files for %{name}
BuildArch:  noarch
Provides:   %{name}-static = %{version}-%{release}
Requires:   cmake-filesystem

%description devel
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%prep
%oreon_sha256
%autosetup -n utfcpp-%{version} -p1

%build
%cmake \
   %{nil}
%cmake_build
pushd tests
%cmake
%cmake_build
popd

%install
%cmake_install
pushd %{buildroot}%{_includedir}
ln -s utf8cpp/utf8.h ./
mkdir utf8
for f in {{un,}checked,core,cpp{11,17,20}}.h ; do
    ln -s ../utf8cpp/utf8/${f} utf8/
done
popd

%check
pushd tests
%ctest
popd

%files devel
%doc API_REFERENCE.md README.md
%license LICENSE
%{_includedir}/utf8.h
%dir %{_includedir}/utf8
%{_includedir}/utf8/checked.h
%{_includedir}/utf8/core.h
%{_includedir}/utf8/cpp11.h
%{_includedir}/utf8/cpp17.h
%{_includedir}/utf8/cpp20.h
%{_includedir}/utf8/unchecked.h
%{_includedir}/utf8cpp
%{_datadir}/cmake/utf8cpp

%changelog
%autochangelog
