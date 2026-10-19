%global source0_hash 4cf79f24567d9e36a325c4855f7e4a5b163db4a9047ad9fd0f9c6e3f30efbdb6
Name:          lxqt-qtplugin
Summary:        Qt plugin framework for LXQt Desktop Suite
Version:       2.4.0
Release:        1%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/lxqt-qtplugin/archive/%{version}/lxqt-qtplugin-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt6XdgIconLoader)
BuildRequires:  pkgconfig(dbusmenu-lxqt)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir lxqt-qtplugin-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
