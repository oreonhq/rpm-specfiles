%global stable_kf6 stable
%global source0_hash e310b9abda691a23767579b35cf468b63dccb7a03ed47cdd63e2ccbb5818fc10
Name:    kmix
Summary:        KDE volume control
Version: 25.12.3
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/%{name}
Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch2:  kmix-21.04.0-autostart_disable.patch
Obsoletes: kdemultimedia-kmix < 6:4.8.80
Provides:  kdemultimedia-kmix = 6:%{version}-%{release}
Conflicts: kde-l10n < 17.03
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
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
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kmix.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kmix.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
