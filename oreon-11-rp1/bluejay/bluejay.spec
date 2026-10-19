%global source0_hash 126300cf0accfc7dcc057af55b03e0805d6089a9dbb54ee339263b57525aa772
%global rdnn_name io.github.ebonjaeger.bluejay
Name:           bluejay
Version:        1.0.3
Release:        5%{?dist}
Summary:        Bluetooth manager written in Qt
License:        MPL-2.0 and CC0-1.0 and CC-BY-SA-4.0 and MIT and GPL-2.0-or-later
URL:            https://github.com/EbonJaeger/bluejay
Source0:        https://github.com/EbonJaeger/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       qt6qml(org.kde.desktop)
Requires:       kf6-kirigami%{?_isa}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
This is a Bluetooth manager and Bluez front-end. With it, you can pair devices,
connect to and remove devices, turn Bluetooth on and off, and more.
Bluejay is powered by the Qt6 graphical toolkit and KDE Frameworks.

Bluejay is meant to be functional and look good.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%conf
%cmake_kf6

%build

%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn_name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
