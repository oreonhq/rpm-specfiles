%global source0_hash 85997b9db83a54c634fe1168950720509078f329c207cdd9befe60e2e2938693
ExcludeArch: %{ix86}
Name:    kirigami-gallery
Version: 26.08.1
Release:        1%{?dist}
Summary:        Gallery application built using Kirigami
License: LGPL-2.1-or-later
URL:     https://apps.kde.org/en/kirigami2.gallery
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:   kf6-kirigami%{?_isa}
Requires:   kf6-kirigami-addons%{?_isa}
Requires:   kf6-kitemmodels%{?_isa}
Requires:   breeze-icon-theme
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Example application which uses all features from kirigami,
including links to the source code, tips on how to use the
components and links to the corresponding HIG pages and
code examples on invent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kirigamigallery --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kirigami2.gallery.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kirigami2.gallery.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
