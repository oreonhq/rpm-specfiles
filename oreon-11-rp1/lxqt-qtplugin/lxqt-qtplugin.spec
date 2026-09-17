%global source0_hash de9d47b2e8a5c813af7ad9c3e097064312c5673f3ddfddf0709a410a622e1b96

Name:          lxqt-qtplugin
Summary:       Qt plugin framework for LXQt Desktop Suite
Version:       2.3.0
Release:       2%{?dist}
License:       LGPL-2.1-only
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/lxqt-qtplugin/archive/%{version}/lxqt-qtplugin-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(lxqt)
BuildRequires: cmake(fm-qt6)
BuildRequires: pkgconfig(libexif)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(Qt6XdgIconLoader)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(dbusmenu-lxqt)
BuildRequires: qt6-qtbase-private-devel

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lxqt-qtplugin-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_libdir}/qt6/plugins/platformthemes/libqtlxqt.so

%changelog
%autochangelog
