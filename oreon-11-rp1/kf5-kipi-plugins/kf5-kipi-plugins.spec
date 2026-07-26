%global source0_hash 7d523b04c52ad299e49ff0cd2e1c1d6158b2423afa50e1ff58dba1223d710dac

%global base_name kipi-plugins

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{base_name}
Summary: Plugins to use with kf5-libkipi applications
Version: 24.05.2
Release: 6%{?dist}

License: GPL-2.0-or-later
URL:     https://apps.kde.org/kipi_plugins/

Source0:        http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: gcc-c++

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5KIO)

BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(Qt5X11Extras)

BuildRequires: cmake(KF5Kipi)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: hicolor-icon-theme

# upgrade path for eol'd kde4-based kipi-plugins
Obsoletes: kipi-plugins < 5.0.0

%description
This package contains plugins to use with Kipi, the KDE Image Plugin
Interface.

%package libs
Summary: Runtime libraries for %{name}
# upgrade path
Obsoletes: kipi-plugins-libs < 5.0.0
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n kipi-plugins-%{version}

# fix ChagngeLog encoding
mv ChangeLog ChangeLog.orig
iconv -f iso-8859-1 -t utf-8 ChangeLog.orig -o ChangeLog

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang all --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/kipiplugins.desktop

%files -n kf5-kipi-plugins -f all.lang
%doc AUTHORS ChangeLog
%doc README TODO NEWS
%license COPYING
%{_kf5_metainfodir}/org.kde.kipi_plugins.metainfo.xml
%{_kf5_datadir}/applications/kipiplugins.desktop
%{_kf5_datadir}/kxmlgui5/kipi/
%{_kf5_datadir}/icons/hicolor/*/apps/kipi-*
%{_kf5_datadir}/kservices5/kipiplugin_*.desktop
%{_kf5_datadir}/kipiplugin_*/

%ldconfig_scriptlets libs

%files libs
%{_kf5_libdir}/libKF5kipiplugins.so*
%{_kf5_qtplugindir}/kipiplugin_*.so
%{_kf5_metainfodir}/org.kde.kipi_plugins.metainfo.xml

%changelog
%autochangelog
