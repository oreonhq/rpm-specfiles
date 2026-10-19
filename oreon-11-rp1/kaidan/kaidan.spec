%global source0_hash b38a64c7b7524a32dffe08eeda034f76d3597a84d8f7afd25c658dab43fb074d
%bcond check 1
Name:           kaidan
Version:        0.16.0
Release:        1%{?dist}
Summary:        A XMPP client based on KDE Framework
License:        GPL-3.0-or-later AND MIT AND Apache-2.0 AND CC-BY-SA-4.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/network/kaidan
Source0:        https://download.kde.org/unstable/kaidan/%{version}/kaidan-%{version}.tar.xz
Provides:       bundled(hsluv-c)
Provides:       bundled(SingleApplication)
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kirigami2-addons%{?_isa}
Requires:       kf6-kquickcharts%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qtwebchannel%{?_isa}
Requires:       qt6-qtwebengine%{?_isa}
Requires:       qt6-qtlocation%{?_isa}
Requires:       kquickimageeditor-qt6%{?_isa}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(QXmppQt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(gstreamer-1.0)
# /oreon:deps
%description
Kaidan is a simple, user-friendly and modern chat client. It uses the open
communication protocol XMPP (Jabber). The user interface makes use of Kirigami
and QtQuick, while the back-end of Kaidan is entirely written in C++ using Qt
and the Qt-based XMPP library QXmpp.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

sed -i 's|Qt6Keychain 0.15|Qt6Keychain|' CMakeLists.txt

%build

%cmake \
    -GNinja \
    -DUSE_KNOTIFICATIONS=ON \
%if %{with check}
    -DBUILD_TESTING=ON \
%else
    -DBUILD_TESTING=OFF \
%endif
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

%if %{with check}
%ctest -E 'PublicGroupChatTest'
%endif
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.0-1
- Prepare for Oreon 11 (RP1)
