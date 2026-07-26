%global source0_hash c15f42592d88e431adea8a255c0c94aaf3783a457c33732e99f96f78694d8396

Name:           kshutdown
Version:        6.2
Release:        1%{?dist}
Summary:        Graphical shutdown utility for Plasma 6
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://kshutdown.sourceforge.io/
Source0:        https://sourceforge.net/projects/%{name}/files/KShutdown/%{version}/%{name}-source-%{version}.zip

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6XmlGui)

%description
KShutdown is a graphical shutdown utility which allows you to turn off
or suspend computer at the specified time. It features various time and delay
options, command line support, and notifications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{cmake_kf6}
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kshutdown.desktop

%files -f %{name}.lang
%doc ChangeLog LICENSE TODO
%{_bindir}/kshutdown
%{_datadir}/applications/kshutdown.desktop
%{_datadir}/icons/hicolor/*/apps/kshutdown.png

%changelog
%autochangelog
