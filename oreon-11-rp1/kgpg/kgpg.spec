Name:    kgpg
Summary: Manage GPG encryption keys
Version: 25.12.3
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/utilities/kgpg/

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros


# pim-related deps below are available only where qtwebengine is
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6TextTemplate)

BuildRequires: cmake(KPim6AkonadiContactWidgets)

BuildRequires: pkgconfig(gpgme)

# when split occured
Conflicts: kdeutils-common < 6:4.7.80

# translations moved here
Conflicts: kde-l10n < 17.03

Obsoletes: kdeutils-kgpg < 6:4.7.80
Provides:  kdeutils-kgpg = 6:%{version}-%{release}

# kgpg (can be either gnupg or gnupg2, we'll default to the latter)
Requires: gnupg2

%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.


%prep
%autosetup -p1


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

# only plasma supports X-KDE-autostart-condition, else it starts unconditionally
# everywhere else, see also https://bugzilla.redhat.com/1427707
desktop-file-edit \
  --add-only-show-in=KDE \
  %{buildroot}%{_kf6_sysconfdir}/xdg/autostart/org.kde.kgpg.desktop


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS
%license LICENSES/*
%{_kf6_bindir}/kgpg
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_sysconfdir}/xdg/autostart/org.kde.kgpg.desktop
%{_kf6_metainfodir}/org.kde.kgpg.appdata.xml
%{_kf6_datadir}/applications/org.kde.kgpg.desktop
%{_kf6_datadir}/config.kcfg/kgpg.kcfg
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kgpg.Key.xml
%{_kf6_datadir}/kio/servicemenus/*.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
