%global source0_hash ab1080e449ff468032b7ba5f203fba1cdca3ab9958c4f9b5451ba0e2c0978f11
%global base_name libkdcraw
Name:    kf5-libkdcraw
Summary:        A C++ interface around LibRaw library
Version: 23.08.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/graphics/%{base_name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Requires: kf5-filesystem
# oreon:deps
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libraw)
# /oreon:deps
%description
Libkdcraw is a C++ interface around LibRaw library used to decode RAW
picture files. More information about LibRaw can be found at
http://www.libraw.org.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt5Gui)
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-libkdcraw-devel -f %{oreon_filedir}/kf5-libkdcraw-devel.list

%changelog

%autochangelog
