%global source3_hash 985b37390cad51f51b03897e503748db5acddfd9442438532cfab1ac9fd1cbcd
%global source2_hash b577baa3476bbe94f0454545e517e1835401d79c5b1105c8e02cf1d4a505e8ec
%global source0_hash 3afae9b103150e2093c221779c32e0d2ce0e8295cf39e4f59bb40a11944e8c0f
%global stable_kf6 stable
%global source1_hash 132bb8faa9265f66ad0bf648ea51ff27c3909b278f061f7c94d601c3bf86b043
ExcludeArch: %{ix86}
Name:           koko
Version:        26.08.1
Release:        1%{?dist}
License:        GPL-2.0-or-later AND GPL-3.0-only AND LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+ AND CC0-1.0 AND LicenseRef-Callaway-BSD
Summary:        An Image gallery application
Url:            https://apps.kde.org/koko/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.geonames.org/export/dump/cities1000.zip
Source2:        https://download.geonames.org/export/dump/admin1CodesASCII.txt
Source3:        https://download.geonames.org/export/dump/admin2Codes.txt
Requires:      kf6-kcoreaddons%{?_isa}
Requires:      kf6-kdeclarative%{?_isa}
Requires:      kf6-kirigami%{?_isa}
Requires:      kf6-kirigami-addons%{?_isa}
Requires:      kf6-purpose%{?_isa}
Requires:      kquickimageeditor-qt6%{?_isa}
Requires:      qt6-qtmultimedia%{?_isa}
Obsoletes:     %{name}-devel < 24.01.80
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup
# Copying these to src dir as per https://invent.kde.org/graphics/koko/-/blob/master/README.md Packaging section.
cp %{SOURCE1} src/
cp %{SOURCE2} src/
cp %{SOURCE3} src/

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
