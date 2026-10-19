%global source0_hash c6fb20753ac27a46bce62e31f7b105b6b99497035830b34a7bba1bc60260c1ca
%if !0%{?bootstrap}
%global tests 1
%endif
%global  base_name konsole
Name:    konsole5
Summary:        KDE Terminal emulator
Version: 23.08.5
Release:        1%{?dist}
License: GPL-2.0-only AND GFDL-1.1-or-later
URL:     http://www.kde.org/applications/system/konsole/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Patch200: konsole-history_location_default.patch
Source10: konsolerc
Obsoletes: konsole < 14.12
Provides:  konsole = %{version}-%{release}
%global maj_ver %(echo %{version} | cut -d. -f1)
%if 0%{?tests}
%endif
Conflicts: kde-l10n < 17.03
Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5NewStuffCore)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  dbus-x11
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package part
Summary: Konsole5 kpart plugin
%description part
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf5 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf5_sysconfdir}/xdg/konsolerc
%find_lang konsole --with-html
grep 'StartupWMClass=' %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop >& /dev/null || \
desktop-file-edit --set-key=StartupWMClass --set-value=konsole %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.konsole.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
test "$(xvfb-run -a %{_target_platform}/src/konsole --version)" = "konsole %{version}" ||:
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 30" ||:
%endif
%files -f %{oreon_filedir}/main.list
%files -n konsole5-part -f %{oreon_filedir}/konsole5-part.list

%changelog

%autochangelog
