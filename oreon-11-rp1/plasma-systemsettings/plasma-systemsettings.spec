%global  base_name systemsettings

Name:    plasma-%{base_name}
Summary: KDE System Settings application
Version: 6.6.2
Release:	2%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Runner)

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(PlasmaActivities)

BuildRequires: cmake(KF6Kirigami2)
BuildRequires: plasma-workspace-devel
Requires:      kf6-kirigami2%{?_isa}

# https://bugzilla.redhat.com/show_bug.cgi?id=1268493
# doc/HTML/en/systemsettings conflicts
Conflicts: kde-workspace < 5.0

# /usr/share/kservices5/settings-system-administration.desktop file conflict
Conflicts: kcm_systemd < 1.2.1-15

Provides:  plasma-systemsettings-devel = %{version}-%{release}
Obsoletes: plasma-systemsettings-devel < 5.20.90

%description
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang systemsettings6 --with-qt --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/kdesystemsettings.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/systemsettings.desktop


%files -f systemsettings6.lang
%license LICENSES/*
%{_bindir}/systemsettings
%{_datadir}/systemsettings/
%{_datadir}/applications/kdesystemsettings.desktop
%{_datadir}/applications/systemsettings.desktop
%{_datadir}/metainfo/org.kde.systemsettings.metainfo.xml
%{_datadir}/zsh/site-functions/_systemsettings
%{_kf6_datadir}/kglobalaccel/systemsettings.desktop
%{_kf6_datadir}/qlogging-categories6/systemsettings.categories
%{_kf6_plugindir}/krunner/krunner_systemsettings.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
