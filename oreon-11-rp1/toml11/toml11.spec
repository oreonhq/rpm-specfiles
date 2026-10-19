%global source0_hash 815bfe6792aa11a13a133b86e7f0f45edc5d71eb78f5fb6686c49c7f792b9049
%bcond test 0
%global debug_package %{nil}
Name:           toml11
Version:        4.4.0
Release:        1%{?dist}
Summary:        TOML for Modern C++
License:        MIT
URL:            https://github.com/ToruNiina/toml11
Source0:        https://github.com/ToruNiina/toml11/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with test}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  ninja-build
# /oreon:deps
%description
toml11 is a header-only TOML parser/encoder for C++11 and later.

%package devel
Summary:        Development files for %{name}
%description devel
Headers and cmake files for %{name}.

%package static
Summary:        Header-only development files for %{name}
Requires:       %{name}-devel = %{version}-%{release}
%description static
Meta package for %{name} header-only library build dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    %if %{with test}
    -Dtoml11_BUILD_TEST=ON \
    %endif
    %{nil}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n toml11-devel -f %{oreon_filedir}/toml11-devel.list
%files -n toml11-static -f %{oreon_filedir}/toml11-static.list
