%global source0_hash 888e41d8dafdd88ec89aeb732a9e7f0270c12015322418bf234836a82a151c08
Name:          kgeotag
Version:       2.0.0
Release:        1%{?dist}
License:       CC-BY-SA-4.0 AND CC0-1.0 AND ODbL-1.0 AND BSD-3-Clause AND GPL-3.0-only
Summary:        Photo geotagging program for KDE Plasma
URL:           https://apps.kde.org/%{name}/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
# oreon:deps
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Marble)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
A Free/Libre Open Source photo geotagging program
built using Qt/C++ and uses the KDE frameworks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kgeotag.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
