%global source0_hash 2cbb10ebac0a0e0efb9d9508c6371fcef0b70302ceb688eeb83824266d9db30c

%undefine __cmake_in_source_build

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: KDE Photo Album 
Name:	 kphotoalbum
Version: 6.0.1
Release: 4%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
# Automatically converted from old format: (GPLv2 or GPLv3) and GFDL - review is highly recommended.
License: (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-GFDL

URL:	 http://kphotoalbum.org/
Source0: https://download.kde.org/stable/kphotoalbum/%{version}/kphotoalbum-%{version}.tar.xz

## upstream patches (lookaside cache)

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: libjpeg-devel
BuildRequires: pkgconfig(exiv2)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Test)

BuildRequires: cmake(Phonon4Qt6)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WidgetsAddons)

BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KDcrawQt6)
BuildRequires: cmake(Marble) >= 24.11.70

%description
A photo album tool. Focuses on three key points:
  * It must be easy to describe a number of images at a time. 
  * It must be easy to search for images. 
  * It must be easy to browse and View the images.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kphotoalbum.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum-import.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kphotoalbum.open-raw.desktop

%files -f %{name}.lang
%license LICENSES/*
%config(noreplace) %{_kf6_sysconfdir}/xdg/kphotoalbumrc
%{_kf6_bindir}/kpa-backup.sh
%{_kf6_bindir}/kphotoalbum
%{_kf6_bindir}/open-raw.pl
%{_kf6_bindir}/kpa-thumbnailtool
%{_kf6_libdir}/libkpabase.so
%{_kf6_libdir}/libkpathumbnails.so
%{_kf6_libdir}/libkpaexif.so
%{_kf6_datadir}/kphotoalbum/
%{_kf6_metainfodir}/org.kde.kphotoalbum.*.xml
%{_kf6_datadir}/applications/org.kde.kphotoalbum.desktop
%{_kf6_datadir}/applications/org.kde.kphotoalbum-import.desktop
%{_kf6_datadir}/applications/org.kde.kphotoalbum.open-raw.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*

%changelog
%autochangelog
