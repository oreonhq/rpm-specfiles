%global source0_hash 38f8e2139a089f00196f288f52f2d0677a6becc218f380b54ca70b6f162398bd
Name: libzim
Version: 9.8.2
Release:        1%{?dist}
License: GPL-2.0-only AND Apache-2.0 AND BSD-3-Clause
Summary:        Reference implementation of the ZIM specification
URL: https://github.com/openzim/%{name}
Source0:        https://github.com/openzim/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Provides: zimlib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: zimlib < %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libicu-devel
BuildRequires:  libzstd-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  xapian-core-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The ZIM library is the reference implementation for the ZIM file
format. It's a solution to read and write ZIM files on many systems
and architectures.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dwerror=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libzim-devel -f %{oreon_filedir}/libzim-devel.list

%changelog

%autochangelog
