%global source0_hash d745a8cd878c89d9bd3227ed027332933bcb9b5415b1d55ff2987c0587fd8182
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name: neochat
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause
URL: https://invent.kde.org/network/%{name}
Summary:        Client for matrix, the decentralized communication protocol
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%ifarch %{qt6_qtwebengine_arches}
%endif
Requires: breeze-icon-theme
Requires: hicolor-icon-theme
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kitemmodels%{?_isa}
Requires: kf6-knotifications%{?_isa}
Requires: kf6-kquickcharts%{?_isa}
Requires: kf6-prison%{?_isa}
Requires: kf6-purpose%{?_isa}
Requires: kf6-sonnet%{?_isa}
Requires: kf6-syntax-highlighting%{?_isa}
Requires: kf6-qqc2-desktop-style%{?_isa}
Requires: kquickimageeditor-qt6%{?_isa}
Requires: qt6-qtlocation%{?_isa}
Requires: qt6-qtmultimedia%{?_isa}
Requires: qt6-qtpositioning%{?_isa}
%ifarch %{qt6_qtwebengine_arches}
Requires: qt6-qtwebview%{?_isa}
%endif
Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
Provides: spectral = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: spectral < 0-19.20201224gitfba0df0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(KUnifiedPush)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Network)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(QuotientQt6)
BuildRequires:  cmark
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libcmark)
# /oreon:deps
%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
