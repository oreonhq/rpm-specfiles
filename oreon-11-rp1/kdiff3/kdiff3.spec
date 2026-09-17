%global source0_hash 4690a35aa933b192751dd590a6b4f53fef3aa950246371112ad6e872f6b26ecb

Name:           kdiff3
Version:        1.12.4
Release:        1%{?dist}
Summary:        Compare + merge 2 or 3 files or directories

License:        GPL-2.0-or-later AND BSD-2-Clause AND CC0-1.0 AND MIT
URL:            https://invent.kde.org/sdk/kdiff3
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  ninja-build

Provides: mergetool

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

%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=ON
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-html --with-man --all-name
chmod -x %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/%{name}
%{_kf6_plugindir}/kfileitemaction/kdiff3fileitemaction.so
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
