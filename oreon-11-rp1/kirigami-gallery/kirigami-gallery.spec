%global source0_hash 9cd49dbcc4fbab9269fe0cdcb49c16ecbb0c76dce02d204380fcdeb9fb60b2a2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kirigami-gallery
Version: 26.08.0
Release: 1%{?dist}
Summary: Gallery application built using Kirigami
License: LGPL-2.1-or-later
URL:     https://apps.kde.org/en/kirigami2.gallery

Source:  https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ItemModels)

Requires:   kf6-kirigami%{?_isa}
Requires:   kf6-kirigami-addons%{?_isa}
Requires:   kf6-kitemmodels%{?_isa}
Requires:   breeze-icon-theme

%description
Example application which uses all features from kirigami,
including links to the source code, tips on how to use the
components and links to the corresponding HIG pages and
code examples on invent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kirigamigallery --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kirigami2.gallery.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kirigami2.gallery.desktop

%files -f kirigamigallery.lang
%doc README.md
%license LICENSE.LGPL-2
%{_kf6_metainfodir}/org.kde.kirigami2.gallery.appdata.xml
%{_kf6_datadir}/applications/org.kde.kirigami2.gallery.desktop
%{_kf6_bindir}/kirigami2gallery

%changelog
%autochangelog
