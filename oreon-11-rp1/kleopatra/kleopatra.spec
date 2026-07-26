%global source0_hash 2d5f02713e07594a8e8c693331776d957e91413ce48ac85c240be91fd670d9ab

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kleopatra
Version: 25.12.3
Release: 1%{?dist}
Summary: KDE certificate manager and unified crypto GUI

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)

URL:     https://invent.kde.org/pim/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)

BuildRequires:  gpgmepp-devel
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  libassuan2-devel

BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6MimeTreeParserWidgets)
BuildRequires:  cmake(KPim6Mbox)

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  hicolor-icon-theme

Requires:       gnupg2
Requires:       gnupg2-smime
%if 0%{?rhel} >= 11 || 0%{?fedora} >= 43
Requires:       gnupg2-scdaemon
%endif

# The -libs subpackage no longer contained anything
Obsoletes:      %{name}-libs < 25.03.80

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kwatchgnupg.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kleopatra.desktop
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/kleopatra_import.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_sysconfdir}/xdg/kleopatradebugcommandsrc
%{_kf6_bindir}/kleopatra
%{_kf6_bindir}/kwatchgnupg
%{_kf6_datadir}/applications/kleopatra_import.desktop
%{_kf6_datadir}/applications/org.kde.kleopatra.desktop
%{_kf6_datadir}/applications/org.kde.kwatchgnupg.desktop
%{_kf6_datadir}/mime/packages/kleopatra-mime.xml
%{_kf6_datadir}/kio/servicemenus/kleopatra_*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kleopatra.*
%{_kf6_datadir}/icons/hicolor/128x128/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/16x16/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/22x22/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/256x256/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/32x32/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/64x64/apps/org.kde.kwatchgnupg.png
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.kwatchgnupg.svg
%{_kf6_datadir}/mime/packages/application-vnd-kde-kleopatra.xml
%{_kf6_datadir}/qlogging-categories6/kleopatra.*
%{_kf6_metainfodir}/org.kde.kleopatra.appdata.xml

%changelog
%autochangelog
