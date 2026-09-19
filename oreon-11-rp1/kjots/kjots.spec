%global source0_hash 3909cc6df5ebeeabe7c9086fc95b54dcd2a1cf5ee1683e0ad6ea799105b4eb08

Name:           kjots
Summary:        KDE Notes application
Version:        6.0.0
Release:        5%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://userbase.kde.org/KJots

Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

# Qt
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)

# KDE Frameworks:
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6TextWidgets)

# KDE PIM
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextEditTextToSpeech)

# Checks:
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
KJots is an application for writing and organizing notes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang kjots --with-kde

%check
for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}/%{_kf6_metainfodir}/org.kde.kjots.appdata.xml

%files -f kjots.lang
%doc README
%license LICENSES/*
%{_kf6_bindir}/kjots
%{_kf6_datadir}/applications/org.kde.kjots.desktop
%{_kf6_datadir}/config.kcfg/kjots.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/kjots.*
%{_kf6_datadir}/kjots/
%{_kf6_metainfodir}/org.kde.kjots.appdata.xml
%{_kf6_qtplugindir}/kcm_kjots.so
%{_kf6_qtplugindir}/kjotspart.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_kjotsplugin.so

%changelog
%autochangelog
