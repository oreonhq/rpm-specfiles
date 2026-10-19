%global source0_hash acbdb57638d75f47b6f07d6ead12af370d3f538858d74523a673548cec771110
%global stable_kf6 stable
%global base_name partitionmanager
%global kf6min 5.240.0
%global qt6min 6.5.0
%global kpmcoremin 24.01
ExcludeArch: %{ix86}
Name:           kde-partitionmanager
Version:        26.08.1
Release:        1%{?dist}
Summary:        KDE Partition Manager
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND CC-BY-4.0 AND CC0-1.0 AND GFDL-1.2-or-later
URL:            https://apps.kde.org/partitionmanager/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPMcore)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
KDE Partition Manager is a utility program to help you manage the disk devices,
partitions and file systems on your computer. It allows you to easily create, 
copy, move, delete, resize without losing data, backup and restore partitions.

KDE Partition Manager supports a large number of file systems, 
including ext2/3/4, reiserfs, NTFS, FAT16/32, jfs, xfs and more.

Starting from version 1.9.50 KDE Partition Manager has become the GUI part of 
KPMcore (KDE PartitionManager core) which contain the libraries used to 
manipulate filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir partitionmanager-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang partitionmanager --with-kde --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*partitionmanager.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
