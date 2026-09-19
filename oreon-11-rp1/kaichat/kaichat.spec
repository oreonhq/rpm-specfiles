%global source0_hash 545980cd4889fced1889e53cf742ac8d538e3aaeb0d7e7bfcb8115b66e0d83a7

Name:           kaichat
Version:        0.5.1
Release:        2%{?dist}
Summary:        Chat interface for AI models such as ollama

License:        CC0-1.0 AND LGPL-2.0-or-later AND MIT AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kaichat/

Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules

# Fedora
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

# Qt
BuildRequires:  cmake(Qt6Widgets)

# KDE Frameworks
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)

# KDE Libraries
BuildRequires:  cmake(KF6TextAutoGenerateText) >= 1.7.0

# Misc
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

# Runtime requirements

%description
%summary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kaichat --all-name --with-html
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.kaichat.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kaichat
%{_kf6_libdir}/libkaichatcore.so.%{version}
%{_kf6_libdir}/libkaichatwidgets.so.%{version}
%{_kf6_datadir}/applications/org.kde.kaichat.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kaichat.png
%{_metainfodir}/org.kde.kaichat.appdata.xml
%{_kf6_datadir}/qlogging-categories6/kaichat.categories
%{_kf6_libdir}/libkaichatcore.so.0
%{_kf6_libdir}/libkaichatwidgets.so.0
%{_kf6_qtplugindir}/autogeneratetext/textplugins/kaichat_webshortcuttextplugin.so
%{_kf6_qtplugindir}/autogeneratetext/toolplugins/textautogeneratetext_currentdatetimeplugin.so
%{_kf6_qtplugindir}/autogeneratetext/textplugins/kaichat_sharetextplugin.so
%{_kf6_datadir}/knotifications6/kaichat.notifyrc

%changelog
%autochangelog
