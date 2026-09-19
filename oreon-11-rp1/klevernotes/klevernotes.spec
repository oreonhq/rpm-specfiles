%global source0_hash 6ed9c29fd621034688860e8f5d8bb1b1941ae89787c88ad8c122af4eeaabb23f

Name:          klevernotes
Version:       1.2.4
Release:       3%{?dist}
License:       BSD-3-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND FSFAP AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only
Summary:       A convergent markdown note taking application
URL:           https://apps.kde.org/klevernotes/

Source0:       https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

Patch0:        no-ksandbox.patch

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6WebEngineQuick)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6IconThemes)

Requires: hicolor-icon-theme
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.kitemmodels)
Requires: qt6qml(QtWebChannel)
Requires: qt6qml(QtWebEngine)

%description
KleverNotes is a note taking and management application
for your mobile and desktop devices. It uses markdown
and allow you to preview your content. Different Markdown
flavors are supported thanks to its custom Markdown parser
based Marked.js, which make the integration of "plugins"
and new features even easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.klevernotes.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/klevernotes
%{_kf6_datadir}/applications/org.kde.klevernotes.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.klevernotes.svg
%{_kf6_metainfodir}/org.kde.klevernotes.metainfo.xml

%changelog
%autochangelog
