
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           colord-kde
Version:        25.12.3
Release:	2%{?dist}
Summary:        Colord support for KDE

License:        CC0-1.0 AND LGPL-3.0-or-later
URL:            https://invent.kde.org/graphics/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ItemModels)

BuildRequires:  pkgconfig(lcms2)
BuildRequires:  libXrandr-devel
BuildRequires:  desktop-file-utils

# colord is a dbus daemon
Requires:       colord
Requires:       plasma-systemsettings
Requires:       kf6-kirigami-addons

%description
KDE support for colord including KDE Daemon module and System Settings module.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang colord-kde

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/{colordkdeiccimporter,kcm_colord}.desktop

%files -f colord-kde.lang
%license COPYING
%doc MAINTAINERS TODO
%{_kf6_bindir}/colord-kde-icc-importer
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_colord.so
%{_kf6_plugindir}/kded/colord.so
%{_kf6_datadir}/applications/colordkdeiccimporter.desktop
%{_kf6_datadir}/applications/kcm_colord.desktop


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
