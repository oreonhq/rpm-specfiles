%global source0_hash 0d6beece342d2610f4f5c4f843964812d0858e2e9d11de97df9a68ad4b278490
%global app_id  org.kde.accessibilityinspector
%global sname   accessibilityinspector
ExcludeArch: %{ix86}
Name:           accessibility-inspector
Version:        25.12.3
Release:        1%{?dist}
Summary:        KDE Accessbility Inspector
License:        LGPL-2.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only) AND CC0-1.0
URL:            https://apps.kde.org/accessibilityinspector/
Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Accessibility Inspector is an inspector for your application accessibility
tree. It lets you check all the items exposed via At-SPI, too.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{sname}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
