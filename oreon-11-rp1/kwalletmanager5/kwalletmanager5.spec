%global source0_hash 8ca9ca7ffa561b9f7211b678f3cdf6d1aa310944b7f1829005347a60b79d6937
%global stable_kf6 stable
%global  base_name kwalletmanager
%global kwalletmanager 1
ExcludeArch: %{ix86}
Name:    kwalletmanager5
Summary:        Manage KDE passwords
Version: 26.08.0
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kwalletmanager5/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Patch1:        kwalletmanager-15.12.1-defaults.patch
%if ! 0%{?flatpak}
%endif
%if 0%{?kwalletmanager}
Obsoletes: kwalletmanager < 15.04.3-100
Provides:  kwalletmanager = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
KDE Wallet Manager is a tool to manage the passwords on your KDE system.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf6 %{?flatpak:-DENABLE_KAUTH=OFF}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kwalletmanager.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kwalletmanager5-kwalletd.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kwalletmanager5.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

* Fri Sep 04 2026 Brandon Lester <boostyconnect@oreonproject.org> - 26.08.0-1
- Latest upstream release

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
