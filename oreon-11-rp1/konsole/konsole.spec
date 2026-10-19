%global source0_hash 64d8aaba741f4412ede26ffbbbe3824523e941b725d3046ec27f510fd42d82e6
%global stable_kf6 stable
%global tests 1
Name:    konsole
Summary:        KDE Terminal emulator
Version: 26.08.1
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://www.kde.org/applications/system/konsole/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch200: konsole-history_location_default.patch
Source10: konsolerc
%if 0%{?tests}
%endif
Conflicts: kde-l10n < 17.03
Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks
Obsoletes: konsole5 < 24.01.75
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package part
Summary: Konsole kpart plugin
%description part
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf6_sysconfdir}/xdg/konsolerc
%find_lang konsole --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konsole.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif
%files -f %{oreon_filedir}/main.list
%files -n konsole-part -f %{oreon_filedir}/konsole-part.list

%changelog

%autochangelog
