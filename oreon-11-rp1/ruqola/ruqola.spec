%global source0_hash 7eb7589143ca770f2280a273a3946d733b5b2359ecf78ceb474f56809956e2db
Name:          ruqola
Version:       2.8.1
Release:        1%{?dist}
Summary:        Qt-based client for Rocket Chat
License:       BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:           https://invent.kde.org/network/%{name}
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Requires: hicolor-icon-theme
Provides: bundled(cmark-rc)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextEmoticonsWidgets)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Ruqola is a Rocket chat client for the KDE desktop.

%package       doc
Summary:       HTML documentation for %{name}
BuildArch:     noarch
%description   doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.ruqola.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ruqola.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n ruqola-doc -f %{oreon_filedir}/ruqola-doc.list

%changelog

%autochangelog
