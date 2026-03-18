Name:    kde-cli-tools
Version: 6.6.2
Release: 1%{?dist}

Summary: Tools based on KDE Frameworks 5 to better interact with the system

License: Artistic-2.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

## upstream patches

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  kf6-rpm-macros

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  plasma-workspace-devel >= %{version}
Requires:       libkworkspace6%{?_isa} >= %{version}

# upgrade path, from when this wasn't split out
Requires:       kdesu = 1:%{version}-%{release}

# unversioned utilitized landed here in 5.23.90, see also
# https://phabricator.kde.org/T14763
# https://invent.kde.org/plasma/kde-cli-tools/-/merge_requests/23
Conflicts: kde-runtime < 17.08.3-23

%description
Provides several KDE and Plasma specific command line tools to allow
better interaction with the system.

%package -n kdesu
Summary: Runs a program with elevated privileges
Epoch: 1
Conflicts: kde-runtime < 14.12.3-2
Conflicts: kde-runtime-docs < 14.12.3-2
%description -n kdesu
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang kdeclitools_qt --with-qt --with-kde --all-name

ln -s %{_kf6_libexecdir}/kdesu %{buildroot}%{_bindir}/kdesu


%files -f kdeclitools_qt.lang
%{_bindir}/kbroadcastnotification
%{_bindir}/kdecp
%{_bindir}/kdecp5
%{_bindir}/kde-inhibit
%{_bindir}/kdemv
%{_bindir}/kdemv5
%{_bindir}/kde-open
%{_bindir}/kde-open5
%{_bindir}/keditfiletype
%{_bindir}/keditfiletype5
%{_bindir}/kinfo
%{_bindir}/kioclient
%{_bindir}/kioclient5
%{_bindir}/kmimetypefinder
%{_bindir}/kmimetypefinder5
%{_bindir}/kstart
%{_bindir}/kstart5
%{_bindir}/ksvgtopng
%{_bindir}/ksvgtopng5
%{_bindir}/plasma-open-settings
%{_kf6_libexecdir}/kdeeject
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_filetypes.so
%{_datadir}/doc/HTML/*/kcontrol6
%{_datadir}/applications/org.kde.keditfiletype.desktop
%{_datadir}/applications/org.kde.plasma.settings.open.desktop
%{_datadir}/applications/kcm_filetypes.desktop
%{_datadir}/zsh/site-functions/_kde-inhibit

%files -n kdesu
%{_bindir}/kdesu
%{_kf6_libexecdir}/kdesu
%{_mandir}/man1/kdesu.1.gz
%{_mandir}/*/man1/kdesu.1.gz
## FIXME: %%lang'ify
%{_datadir}/doc/HTML/*/kdesu


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
