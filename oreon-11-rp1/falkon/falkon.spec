%global stable_kf6 stable
%global source0_hash 25f90957335058fff8536b511135e36d96e74c49fab45690be89b994015777b5
%bcond python 0
Name:           falkon
Version:        25.12.3
Release:        1%{?dist}
Summary:        Modern web browser
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://www.falkon.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:         falkon-3.1.0-native-scrollbars.patch
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
%if %{with python}
%endif
Requires:       qt6-qtbase%{?_isa} >= %(echo %{_qt6_version} | cut -d. -f-2)
%global qtwebengine_version %(pkg-config --modversion Qt6WebEngineCore 2>/dev/null || echo 6.6)
Requires:       qt6-qtwebengine%{?_isa} >= %(echo %{qtwebengine_version} | cut -d. -f-2)
Requires:       hicolor-icon-theme
Provides:       bundled(qtsingleapplication-qt6)
%global __provides_exclude_from ^%{_kf6_qtplugindir}/falkon/.*$
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(Shiboken6Tools)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  xcb-util-devel
# /oreon:deps
%package gnome-keyring
Summary: gnome-keyring plugin for %{name}
BuildRequires:  pkgconfig(gnome-keyring-1)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gnome-keyring
%{summary}.

%package kde
Summary: KDE Frameworks Integration plugin for %{name}
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6JobWidgets)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description kde
Plugin for Falkon adding support for:
- storing passwords securely in KWallet,
- additional URL protocols using KIO (e.g., man:, info:, gopher:, etc.),
- a "Share page" menu using the KDE Purpose Framework,
- intercepting crashes with KCrash, bringing up the DrKonqi crash handler.

%description
Falkon is a modern web browser based on QtWebEngine (which is itself based on
the Chromium core, i.e., Blink) and the Qt framework. It is designed to be
lightweight and fast and offers advanced functions such as
- an integrated advertisement blocker,
- a search engine manager,
- a SSL certificate manager,
- speed dial
- theming support, and
- seamless integration into your desktop environment.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%if %{with python}
# delete falkon_hellopython and falkon_helloqml translations, those plugins are
# not shipped
rm -f po/*/falkon_hello*.po
%else
# delete all Python plugins' and falkon_helloqml translations, those plugins are
# not shipped
rm -rf po
%endif

%build

%if %{with python}
%cmake_kf6
%else
%cmake_kf6 -DBUILD_PYTHON_SUPPORT=OFF
%endif
%cmake_build
%install
%cmake_install
find %{buildroot}/%{_datadir}/locale/ -name "*.qm" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.qm\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >%{name}.lang
%if 0%{with python}
find %{buildroot}/%{_datadir}/locale/ -name "*.mo" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.mo\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >>%{name}.lang
%endif
desktop-file-install \
    --add-mime-type="x-scheme-handler/http;x-scheme-handler/https;" \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.kde.falkon.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.falkon.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n falkon-gnome-keyring -f %{oreon_filedir}/falkon-gnome-keyring.list
%files -n falkon-kde -f %{oreon_filedir}/falkon-kde.list

%changelog

%autochangelog
