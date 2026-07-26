%global source0_hash b5e677f415b3812f2dca96f6d26afb62d97ffcd759b6318c29d76c436dc58c27

Name:          ruqola
Version:       2.6.0
Release:       3%{?dist}
Summary:       Qt-based client for Rocket Chat

License:       BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:           https://invent.kde.org/network/%{name}

Source:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# Qt
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6NetworkAuth)
BuildRequires: cmake(Qt6MultimediaWidgets)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6Test)

# KDE Frameworks
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6TextTranslator)
BuildRequires: cmake(KF6TextAutoCorrectionWidgets)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KF6TextEmoticonsWidgets)
BuildRequires: cmake(KF6TextUtils)
BuildRequires: cmake(KF6TextCustomEditor)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6DocTools)
# Not in Fedora
# BuildRequires: cmake(KLLMWidgets)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6StatusNotifierItem)

BuildRequires: cmake(PlasmaActivities)

Requires: hicolor-icon-theme

Provides: bundled(cmark-rc)

%description
Ruqola is a Rocket chat client for the KDE desktop.

%package       doc
Summary:       HTML documentation for %{name}
BuildArch:     noarch
%description   doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.ruqola.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ruqola.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/ruqola
%{_kf6_datadir}/applications/org.kde.ruqola.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/ruqola.png
%{_kf6_datadir}/knotifications6/ruqola.notifyrc
%{_kf6_datadir}/messageviewer/openurlwith/ruqola.openurl
%{_kf6_datadir}/qlogging-categories6/ruqola.{categories,renamecategories}
%{_kf6_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.%{version}
%{_kf6_libdir}/{librocketchatrestapi-qt,libruqolacore,libruqolawidgets}.so.0
%{_kf6_metainfodir}/org.kde.ruqola.appdata.xml
%{_kf6_qtplugindir}/ruqolaplugins/
%{_kf6_libdir}/libcmark-rc-copy.so.*

%files doc
%dir %{_docdir}/HTML/en/ruqola
%{_docdir}/HTML/en/ruqola/index.cache.bz2
%{_docdir}/HTML/en/ruqola/index.docbook

%changelog
%autochangelog
