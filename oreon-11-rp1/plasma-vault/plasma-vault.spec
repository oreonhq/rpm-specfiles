
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-vault
Summary: Plasma Vault offers strong encryption features in a user-friendly way
Version: 6.6.2
Release:	2%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

# Upstream changes

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(KF6KirigamiPlatform)

# Plasma

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

# Qt
BuildRequires:  cmake(Qt6Quick)

## Runtime backends
Recommends: cryfs
Recommends: fuse-encfs
Requires: gocryptfs

%description
Plasma Vault allows to lock and encrypt sets of documents and hide them from
prying eyes even when the user is logged in.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_plugindir}/kded/plasmavault.so
%dir %{_qt6_plugindir}/plasma/applets/
%{_qt6_plugindir}/plasma/applets/org.kde.plasma.vault.so
%{_qt6_plugindir}/kf6/kfileitemaction/plasmavaultfileitemaction.so
%{_kf6_datadir}/plasma/plasmoids/org.kde.plasma.vault/

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
