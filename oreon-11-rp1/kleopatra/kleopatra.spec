%global stable_kf6 stable
%global source0_hash 2d5f02713e07594a8e8c693331776d957e91413ce48ac85c240be91fd670d9ab
ExcludeArch: %{ix86}
Name:    kleopatra
Version: 25.12.3
Release:        1%{?dist}
Summary:        KDE certificate manager and unified crypto GUI
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       gnupg2
Requires:       gnupg2-smime
Obsoletes:      %{name}-libs < 25.03.80
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6MimeTreeParserWidgets)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gpgmepp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libassuan2-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
