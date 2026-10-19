%global source0_hash 370b45b5e05a91960df0aeb9c9481ae05846aab92ab2d4ec66945a0da4216888
Name:           libwacom
Version:        2.20.0
Release:        1%{?dist}
Summary:        Tablet Information Client Library
Requires:       %{name}-data
License:        HPND
URL:            https://github.com/linuxwacom/libwacom
Source0:        https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Requires:       %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  libevdev-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
%{name} is a library that provides information about Wacom tablets and
tools. This information can then be used by drivers or applications to tweak
the UI or general settings to match the physical tablet.

%package devel
Summary:        Tablet Information Client Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Tablet information client library development package.

%package data
Summary:        Tablet Information Client Library Data Files
BuildArch:      noarch
%description data
Tablet information client library data files.

%package utils
Summary:        Tablet Information Client Library Utilities Package
Requires:       %{name} = %{version}-%{release}
Requires:       python3-libevdev python3-pyudev
%description utils
Utilities to handle and/or debug libwacom devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dtests=disabled -Ddocumentation=disabled
%meson_build
%install
%meson_install
install -d ${RPM_BUILD_ROOT}/%{_udevrulesdir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libwacom-devel -f %{oreon_filedir}/libwacom-devel.list
%files -n libwacom-data -f %{oreon_filedir}/libwacom-data.list
%files -n libwacom-utils -f %{oreon_filedir}/libwacom-utils.list

%changelog

%autochangelog
