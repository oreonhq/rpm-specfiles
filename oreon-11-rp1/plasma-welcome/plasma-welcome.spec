%global orgname org.kde.plasma-welcome

Name:           plasma-welcome
Version:        6.6.2
Release:	2%{?dist}
License:        GPL-2.0-or-later and BSD-3-Clause
Summary:        Plasma Welcome
Url:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

# Upstream patches

BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Svg)

BuildRequires:  cmake(Plasma)

Requires:       kf6-kuserfeedback

Provides:       plasma-welcome-app = %{version}-%{release}
Obsoletes:      plasma-welcome-app < 5.27.0-2

%description
A Friendly onboarding wizard for Plasma.

%prep
%autosetup -n %{name}-%{version} -p1
# It is for generate pot file for translate so we can ignore it.
rm Messages.sh

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html
rm -fv %{buildroot}%{_kf6_libdir}/libplasma-welcome-publicplugin.a
%check
# commented out until upstream fixes duplicate entries
#appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{orgname}.*.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{orgname}.desktop

%files -f %{name}.lang
%license LICENSES/{BSD-3-Clause.txt,GPL-2.0-or-later.txt,FSFAP.txt}
%doc README.md
%{_kf6_bindir}/plasma-welcome
%{_kf6_datadir}/applications/%{orgname}.desktop
%{_kf6_metainfodir}/%{orgname}.*.xml
%{_kf6_plugindir}/kded/kded_plasma_welcome.so
%{_kf6_qmldir}/org/kde/plasma/welcome/
%{_kf6_datadir}/qlogging-categories6/welcome.categories


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
