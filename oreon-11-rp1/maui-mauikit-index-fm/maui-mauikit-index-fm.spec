%global source0_hash 889a0b960377fb97d784421958d55d22ada803894bcce2a3e0214314bf653f87
Name:          maui-mauikit-index-fm
Version:       4.0.0
Release:        1%{?dist}
License:       BSD-3-Clause AND MIT AND GPL-2.0-or-later AND GPL-3.0-or-later AND CC0-1.0
Summary:        Simple file manager for desktops and Plasma Mobile
URL:           https://apps.kde.org/%{name}/
Source0:        https://download.kde.org/stable/maui/index/%{version}/index-fm-%{version}.tar.xz
Requires:      hicolor-icon-theme
Requires:      maui-mauikit-filebrowsing
Requires:      maui-mauikit-archiver
Requires:      maui-mauikit-terminal
Requires:      maui-mauikit-documents
Requires:      kf6-purpose
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitArchiver4)
BuildRequires:  cmake(MauiKitDocuments4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(MauiKitTerminal4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  qt6-qtdeclarative-devel
# /oreon:deps
%description
Index is a file manager that works on desktops, Android and Plasma Mobile.
Index lets you browse your system files and applications and preview your
music, text, image and video files and share them with external applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir index-fm-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang index-fm --with-man --with-qt --all-name
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.index.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
