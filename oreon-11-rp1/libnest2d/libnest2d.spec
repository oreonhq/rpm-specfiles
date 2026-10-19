%global source0_hash df106300a7b1d4a9e35fe122dfca3432ffd02249e65043f429da5dadc5284382
Name:           libnest2d
%global commit  da4782500da4eb8cb6e38e5e3f10164ec5a59778
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Version:        0.4^20200805git%{shortcommit}
Release:        1%{?dist}
Summary:        Library for the 2D bin packaging problem
License:        LGPL-3.0-only
URL:            https://github.com/tamasmeszaros/libnest2d
Source0:        https://github.com/tamasmeszaros/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{url}/pull/18.patch
%global debug_package %{nil}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(nlopt)
BuildRequires:  polyclipping-devel
# /oreon:deps
%description
A library and framework for the 2D bin packaging problem.

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       boost-devel
Requires:       polyclipping-devel
Requires:       pkgconfig(nlopt)
%description devel
A library and framework for the 2D bin packaging problem.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1
sed -i -e "s/ lib\([^n]\)/ "%{_lib}"\1/" CMakeLists.txt

%build

%cmake -DLIBNEST2D_HEADER_ONLY=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libnest2d-devel -f %{oreon_filedir}/libnest2d-devel.list

%changelog

%autochangelog
