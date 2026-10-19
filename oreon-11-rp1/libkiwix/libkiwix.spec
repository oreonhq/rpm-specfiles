%global source0_hash cff1eb06d62ab42e1720a49f473b7d9364f02ee77a8a455c9adb26db419e0fff
Name: libkiwix
Version: 14.2.1
Release:        1%{?dist}
License: GPL-3.0-or-later
Summary:        Common code base for all Kiwix ports
URL: https://github.com/kiwix/%{name}
Source0:        https://github.com/kiwix/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Provides: kiwix-lib = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kiwix-lib < %{?epoch:%{epoch}:}%{version}-%{release}
# oreon:deps
BuildRequires:  aria2
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libzim-devel
BuildRequires:  meson
BuildRequires:  mustache-devel
BuildRequires:  ninja-build
BuildRequires:  pugixml-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The Kiwix library provides the Kiwix software core. It contains
the code shared by all Kiwix ports.

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
%files -n libkiwix-devel -f %{oreon_filedir}/libkiwix-devel.list

%changelog

%autochangelog
