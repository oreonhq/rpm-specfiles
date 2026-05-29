%global source0_hash none

# 
ExcludeArch: %{ix86}

Name:           kio-admin
Version:        26.04.1
Release:        1%{?dist}
Summary:        Manage files as administrator using the admin:// KIO protocol
License:        (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
URL:            https://invent.kde.org/system/kio-admin

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  cmake

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  zstd
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  libatomic


%description
kio-admin implements a new protocol "admin:///" 
which gives administrative access
to the entire system. This is achieved by talking, 
over dbus, with a root-level
helper binary that in turn uses 
existing KIO infrastructure to run file://
operations in root-scope.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build

%install
%cmake_install
%find_lang kio6_admin %{name}.lang

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_metainfodir}/org.kde.kio.admin.metainfo.xml
%dir %{_kf6_plugindir}/kfileitemaction/
%{_kf6_plugindir}/kfileitemaction/kio-admin.so
%dir %{_kf6_plugindir}/kio/
%{_kf6_plugindir}/kio/admin.so
%{_kf6_libexecdir}/kio-admin-helper
%{_kf6_datadir}/dbus-1/system.d/org.kde.kio.admin.conf
%{_kf6_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_kf6_datadir}/polkit-1/actions/org.kde.kio.admin.policy

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
