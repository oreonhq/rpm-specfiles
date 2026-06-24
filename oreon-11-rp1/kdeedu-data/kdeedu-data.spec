%global source0_hash none

Name:    kdeedu-data
Summary: Shared icons, artwork and data files for educational applications
Version: 26.04.2
Release: 1%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://invent.kde.org/education/%{name}
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildArch: noarch

BuildRequires: kde-filesystem
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
# ECM macro used in kdeedu-data needs qmake
BuildRequires: qt6-qtbase-devel

Requires: hicolor-icon-theme

%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install


%files
%license COPYING
%{_kf6_datadir}/apps/kvtml/
%{_datadir}/icons/hicolor/*/*/*


%changelog
%autochangelog

