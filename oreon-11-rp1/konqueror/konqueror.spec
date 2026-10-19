%global stable_kf6 stable
%global source0_hash 8f383beada857b522a59b9259ae1f1f83554c5d25d3c39a39fb6f172ec0f889d
Name:    konqueror
Version: 25.12.3
Release:        1%{?dist}
Summary:        KDE File Manager and Browser
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-GFDL
URL:     https://apps.kde.org/konqueror/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
%if 0%{?ninja}
%else
%endif
%if 0%{?tests}
%endif
Requires:      kwebenginepart%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release} 
Requires:      hicolor-icon-theme
Requires:      keditbookmarks
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package libs
Summary:       Runtime libraries for %{name}
Requires:      %{name} = %{version}-%{release}
%description libs
%{summary}.

%package -n kwebenginepart
Summary:  A KPart based on QtWebEngine
%description -n kwebenginepart
KWebEnginePart is a web browser component for KDE (KPart)
based on (Qt)WebEngine. You can use it for example for
browsing the web in Konqueror.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -Wno-dev \
  %{?ninja:-G Ninja} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles kwebenginepart usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konqueror.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient_html.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient_war.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/konqbrowser.desktop
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a \
%if 0%{?ninja}
ninja test -v -C %{_target_platform} ||:
%else
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n konqueror-devel -f %{oreon_filedir}/konqueror-devel.list
%files -n konqueror-libs -f %{oreon_filedir}/konqueror-libs.list
%files -n kwebenginepart -f %{oreon_filedir}/kwebenginepart.list

%changelog

%autochangelog
