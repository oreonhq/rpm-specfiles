Name:    kaccounts-providers
Version: 25.12.3
Release:	2%{?dist}
Summary: Additional service providers for KAccounts framework
# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://invent.kde.org/network/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Upstream patches

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  extra-cmake-modules
BuildRequires:  intltool
BuildRequires:  kaccounts-integration-qt6-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-rpm-macros

BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6WebEngineQuick)
BuildRequires:  qcoro-qt6-devel

Requires:       signon-ui

# google provider
Requires:       signon-plugin-oauth2

# https://pagure.io/fedora-kde/SIG/issue/66
Supplements:    kaccounts-integration-qt6

# switched to arch'd pkg
Obsoletes: kaccounts-providers < 15.12.0

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name


%files -f %{name}.lang
%license LICENSES/*
%config %{_sysconfdir}/signon-ui/webkit-options.d/*
%{_datadir}/accounts/providers/kde/
%dir %{_kf6_datadir}/kpackage/genericqml
%{_kf6_datadir}/kpackage/genericqml/org.kde.kaccounts.owncloud/
%dir %{_qt6_plugindir}/kaccounts/
%dir %{_qt6_plugindir}/kaccounts/ui/
%{_qt6_plugindir}/kaccounts/ui/nextcloud_plugin_kaccounts.so
%{_datadir}/accounts/services/kde/
%{_qt6_plugindir}/kaccounts/ui/owncloud_plugin_kaccounts.so
%{_kf6_datadir}/kpackage/genericqml/org.kde.kaccounts.nextcloud/
%{_kf6_datadir}/icons/hicolor/*/*/*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
