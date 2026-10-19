%global source0_hash 63cbda2b6c78dd14ee8d0547e6061e2657b581c709984927abba2257f897bbb4
%global gitcommit 1912c8055d9f607916e0c6fc568e2c0ee0336493
%global gitdate 20231028.022709
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
Name:          fielding
Version:       0.1~%{gitdate}.%{shortcommit}
Release:        1%{?dist}
Summary:        A simple REST API testing tool
License:       CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:           https://apps.kde.org/en-gb/%{name}/
Source0:        https://invent.kde.org/utilities/%{name}/-/archive/%{shortcommit}/%{name}-%{shortcommit}.tar.gz
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{shortcommit} -p1

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.fielding.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.fielding.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 25 2025 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-7
- Rebuild (qt6)

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-5
- Rebuild (qt6)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1~20231028.022709.1912c80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-3
- Rebuild (qt6)

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 0.1~20231028.022709.1912c80-2
- Rebuild (qt6)

* Thu Oct 12 2023 Steve Cossette <farchord@gmail.com> - 0.1~20231028.022709.1912c80-1
- v0.1
