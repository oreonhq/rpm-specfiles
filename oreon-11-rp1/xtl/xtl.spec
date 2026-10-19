%global source0_hash 8fb38d6a5856aab5740d2ccb3d791d289f648d4cc506b94a1338fe5fce100c11
%global debug_package %{nil}
Name:           xtl
Version:        0.8.2
Release:        1%{?dist}
License:        BSD-3-Clause
Summary:        QuantStack tools library
Url:            https://github.com/QuantStack/xtl
Source0:        https://github.com/QuantStack/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3dist(breathe)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
# /oreon:deps
%description
Basic tools (containers, algorithms) used by other QuantStack packages.

%package devel
Summary:        %{summary}
Provides:       xtl-static = %{version}-%{release}
Requires:       cmake-filesystem
%description devel
Development files for %{name} library.

%package doc
Summary:        %{summary}
%description doc
Documentation files for %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_TESTS=ON
%cmake_build
pushd docs
make html SPHINXBUILD=sphinx-build-3
rm build/html/.buildinfo
popd
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build --target xtest
%files -f %{oreon_filedir}/main.list
%files -n xtl-devel -f %{oreon_filedir}/xtl-devel.list
%files -n xtl-doc -f %{oreon_filedir}/xtl-doc.list

%changelog

%autochangelog
