%global source0_hash ce1a91277edf256e9fc6a90fbc486dabd951b329c81d1c9328b0fa3bf06474c8
%global stable_kf6 stable
Name:           kio-gdrive
Version:        26.08.1
Release:        1%{?dist}
Summary:        An Google Drive KIO slave for KDE
License:        GPL-2.0-or-later
URL:            https://community.kde.org/KIO_GDrive
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Requires:       kaccounts-providers
Requires:       accounts-qml-module-qt6
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  kf6-rpm-macros
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  libkgapi-devel
# /oreon:deps
%description
Provides KIO Access to Google Drive using the gdrive:/// protocol.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kio6_gdrive --all-name --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/remoteview/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
