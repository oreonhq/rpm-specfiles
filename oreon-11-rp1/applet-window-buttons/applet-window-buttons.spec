%global source0_hash 6d9c724565181f6cecb129d769bb053ecee487d8d1dd1d85b8a39b5f4e26d825

%global gitdate 20250224
%global commit0 b114cf23da4411d19c1f1600a98bfab5369fd950
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global orig_name org.kde.windowbuttons

Name:           applet-window-buttons
Version:        0.14.0^%{gitdate}.%{shortcommit0}
Release:        1%{?dist}
Summary:        Plasma 6 applet to show window buttons in panels
License:        GPL-2.0-or-later
URL:            https://github.com/moodyhunter/applet-window-buttons6
Source0:        https://github.com/moodyhunter/applet-window-buttons6/archive/%{commit0}/%{name}-%{commit0}.tar.gz

# http://github.com/moodyhunter/applet-window-buttons6/pull/31
Patch0:         plasma6.6.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KDecoration3)
BuildRequires:  kwin-devel

Provides:       applet-window-buttons6 = %{version}-%{release}

%description
This is a Plasma 5 applet that shows the current window appmenu in
one's panels. This plasmoid is coming from Latte land, but it can also
support Plasma panels.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n applet-window-buttons6-%{commit0} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/plasma/plasmoids/%{orig_name}/metadata.desktop

%files
%license LICENSE
%{_kf6_datadir}/plasma/plasmoids/%{orig_name}
%{_qt6_qmldir}/org/kde/appletdecoration

%changelog
%autochangelog
