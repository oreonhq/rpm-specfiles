
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name: neochat
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND BSD-3-Clause
URL: https://invent.kde.org/network/%{name}
Summary: Client for matrix, the decentralized communication protocol
Source: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6TextToSpeech)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebView)
%endif
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(QuotientQt6)
BuildRequires: cmake(QCoro6Core)
BuildRequires: cmake(QCoro6Network)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KUnifiedPush)

BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libcmark)

BuildRequires: cmake
BuildRequires: cmark
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: ninja-build

Requires: breeze-icon-theme
Requires: hicolor-icon-theme
# QML module dependencies
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

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -p1

%build
%cmake_kf6 -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-qt --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/krunner/dbusplugins/*.desktop
%{_kf6_datadir}/qlogging-categories6/neochat.categories
%{_libdir}/qt6/plugins/kf6/purpose/neochatshareplugin.so
%{_mandir}/man1/neochat.1*
%{_kf6_datadir}/dbus-1/services/org.kde.neochat.service

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
