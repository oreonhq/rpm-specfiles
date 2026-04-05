Name:    plasma-browser-integration
Summary: %{name} provides components necessary to integrate browsers into the Plasma Desktop
Version: 6.6.2
Release:	2%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

## downstream patches

## upstream patches

## upstreamable patches

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  plasma-workspace-devel >= %{version}

Supplements: (plasma-workspace and chromium)
Supplements: (plasma-workspace and firefox)

%description
%{name} coupled with a browser plugin provides integration of the browser in the desktop.

For more information, see
https://community.kde.org/Plasma/Browser_Integration


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6 \
  -DMOZILLA_DIR:PATH=%{_libdir}/mozilla \
  -DLIBREWOLF_DIR:PATH=%{_libdir}/librewolf \
  -DWATERFOX_DIR:PATH=%{_libdir}/waterfox
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%config %{_sysconfdir}/chromium/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.kde.plasma.browser_integration.json
%config %{_sysconfdir}/opt/edge/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/waterfox/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_bindir}/plasma-browser-integration-host
%{_libdir}/mozilla/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_libdir}/librewolf/native-messaging-hosts/org.kde.plasma.browser_integration.json
%{_kf6_plugindir}/kded/browserintegrationreminder.so
%{_kf6_datadir}/krunner/dbusplugins/plasma-runner-browserhistory.desktop
%{_kf6_datadir}/krunner/dbusplugins/plasma-runner-browsertabs.desktop
%{_kf6_datadir}/applications/org.kde.plasma.browser_integration.host.desktop
%{_kf6_qtplugindir}/kf6/kded/browserintegrationflatpakintegrator.so

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
