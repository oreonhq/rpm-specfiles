%global source0_hash 4d7dfe712004f1041481cc0a752c01c494983adf87f6df78568ba7198f7dc5f6
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:           kio-admin
Version:        26.08.0
Release:        1%{?dist}
Summary:        Manage files as administrator using the admin:// KIO protocol
License:        (GPL-2.0-only or GPL-3.0-only) and BSD-3-Clause and CC0-1.0 and FSFAP
URL:            https://invent.kde.org/system/kio-admin
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libatomic
BuildRequires:  zstd
# /oreon:deps
%description
kio-admin implements a new protocol "admin:///" 
which gives administrative access
to the entire system. This is achieved by talking, 
over dbus, with a root-level
helper binary that in turn uses 
existing KIO infrastructure to run file://
operations in root-scope.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang kio6_admin %{name}.lang
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
