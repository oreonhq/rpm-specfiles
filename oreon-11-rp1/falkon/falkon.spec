%global source0_hash 25f90957335058fff8536b511135e36d96e74c49fab45690be89b994015777b5

# build Python plugins (disabled by default due to #2048781)
%bcond python 0

Name:           falkon
Version:        25.12.3
Release:        1%{?dist}
Summary:        Modern web browser

# Files in src/lib/opensearch and src/lib/3rdparty are GPLv2+
# Files in src/plugins/MouseGestures/3rdparty are BSD (2 clause)
# Automatically converted from old format: GPLv3+ and BSD - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-BSD
URL:            https://www.falkon.org/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# reenable native scrollbars by default (upstream disabled them in 2.1.2)
Patch0:         falkon-3.1.0-native-scrollbars.patch

## upstream patches

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6WebChannel)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(KF6Archive)

BuildRequires:  openssl-devel
BuildRequires:  xcb-util-devel

%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  cmake(PySide6)
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(Shiboken6Tools)
BuildRequires:  cmake(KF6I18n)
%endif

# require the correct minimum versions of Qt, symbol versioning does not work
Requires:       qt6-qtbase%{?_isa} >= %(echo %{_qt6_version} | cut -d. -f-2)
%global qtwebengine_version %(pkg-config --modversion Qt6WebEngineCore 2>/dev/null || echo 6.6)
Requires:       qt6-qtwebengine%{?_isa} >= %(echo %{qtwebengine_version} | cut -d. -f-2)

# directory ownership
Requires:       hicolor-icon-theme

# forked version that uses D-Bus instead of lock files (see also #1551678)
Provides:       bundled(qtsingleapplication-qt6)

%global __provides_exclude_from ^%{_kf6_qtplugindir}/falkon/.*$

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

# translations (find_lang_kf6 does not support --all-name, so adapt it)
find %{buildroot}/%{_datadir}/locale/ -name "*.qm" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.qm\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >%{name}.lang
%if 0%{with python}
find %{buildroot}/%{_datadir}/locale/ -name "*.mo" -type f | sed 's:%{buildroot}/::;s:%{_datadir}/locale/\([a-zA-Z_\@]*\)/LC_MESSAGES/\([^/]*\.mo\):%lang(\1) %{_datadir}/locale/\1/LC_MESSAGES/\2:' >>%{name}.lang
%endif

desktop-file-install \
    --add-mime-type="x-scheme-handler/http;x-scheme-handler/https;" \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/org.kde.falkon.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.falkon.appdata.xml

%files -f %{name}.lang
%doc README.md CHANGELOG
%license COPYING
%{_kf6_bindir}/falkon
%{_kf6_libdir}/libFalkonPrivate.so.*
%dir %{_kf6_qtplugindir}/falkon/
%{_kf6_qtplugindir}/falkon/AutoScroll.so
%{_kf6_qtplugindir}/falkon/FlashCookieManager.so
%{_kf6_qtplugindir}/falkon/GreaseMonkey.so
%{_kf6_qtplugindir}/falkon/MouseGestures.so
%{_kf6_qtplugindir}/falkon/PIM.so
%{_kf6_qtplugindir}/falkon/StatusBarIcons.so
%{_kf6_qtplugindir}/falkon/TabManager.so
%{_kf6_qtplugindir}/falkon/VerticalTabs.so
%if %{with python}
%{_kf6_qtplugindir}/falkon/i18n.py
%{_kf6_qtplugindir}/falkon/middleclickloader/
%{_kf6_qtplugindir}/falkon/runaction/
%endif
%{_kf6_metainfodir}/org.kde.falkon.appdata.xml
%{_kf6_datadir}/applications/org.kde.falkon.desktop
%{_kf6_datadir}/bash-completion/
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/falkon/

%files gnome-keyring
%{_kf6_qtplugindir}/falkon/GnomeKeyringPasswords.so

%files kde
%{_kf6_qtplugindir}/falkon/KDEFrameworksIntegration.so

%changelog
%autochangelog
