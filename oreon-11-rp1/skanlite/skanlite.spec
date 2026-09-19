%global source0_hash e30dfc3601545291fc3d813ceaafcee91d0b850dcb54688be49a0f431779501f

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           skanlite
Version:        25.12.3
Release:        1%{?dist}
Summary:        Lightweight scanning program
# Actually: GPLv2 or GPLv3 or any later Version approved by KDE e.V.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kde.org/applications/graphics/%{name}/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libpng-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(KF6Crash)

%description
Skanlite is a light-weight scanning application based on libksane.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html
install -Dpm 0644 logo.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSES
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.kde.skanlite.svg
%{_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
%autochangelog
