%global source0_hash 76b71fa853e24d6ab521caaf0e180faca06aa5a0e4103c78a59bc932f4c55381
%global stable_kf6 stable
Name:    kgpg
Summary:        Manage GPG encryption keys
Version: 26.08.1
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/utilities/kgpg/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Conflicts: kdeutils-common < 6:4.7.80
Conflicts: kde-l10n < 17.03
Obsoletes: kdeutils-kgpg < 6:4.7.80
Provides:  kdeutils-kgpg = 6:%{version}-%{release}
Requires: gnupg2
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gpgme)
# /oreon:deps
%description
KGpg is a simple interface for GnuPG, a powerful encryption utility.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
desktop-file-edit \
  --add-only-show-in=KDE \
  %{buildroot}%{_kf6_sysconfdir}/xdg/autostart/org.kde.kgpg.desktop
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
