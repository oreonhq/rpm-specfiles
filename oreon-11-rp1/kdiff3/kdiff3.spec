%global source0_hash edeaa2313cb74b650958d24cd98b300b73173ac8a9c87067de62babf02baa37c
Name:           kdiff3
Version:        1.12.6
Release:        1%{?dist}
Summary:        Compare + merge 2 or 3 files or directories
License:        GPL-2.0-or-later AND BSD-2-Clause AND CC0-1.0 AND MIT
URL:            https://invent.kde.org/sdk/kdiff3
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Provides: mergetool
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  qt6-qt5compat-devel
# /oreon:deps
%description
KDiff3 is a program that
- compares and merges two or three input files or directories,
- shows the differences line by line and character by character (!),
- provides an automatic merge-facility and
- an integrated editor for comfortable solving of merge-conflicts
- has support for KDE-KIO (ftp, sftp, http, fish, smb)
- and has an intuitive graphical user interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DBUILD_WITH_QT6:BOOL=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html --with-man --all-name
chmod -x %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
