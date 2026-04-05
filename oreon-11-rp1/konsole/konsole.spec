%if  0%{?rhel} && 0%{?rhel} >= 10
# Tests require x11
# x11 is not in RHEL 10
%global tests 0
%else
%global tests 1
%endif

Name:    konsole
Summary: KDE Terminal emulator
Version: 25.12.3
Release:	2%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://www.kde.org/applications/system/konsole/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

## upstream patches

## downstream patches
Patch200: konsole-history_location_default.patch
# custom konsolerc that sets default to cache as well
Source10: konsolerc

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(zlib)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Pty)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: libappstream-glib
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: libicu-devel

%if 0%{?tests}
BuildRequires: pkgconfig(x11)
BuildRequires: appstream
BuildRequires: xorg-x11-server-Xvfb dbus-x11
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks

Obsoletes: konsole5 < 24.01.75

%description
%{summary}.

%package part
Summary: Konsole kpart plugin
%description part
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf6_sysconfdir}/xdg/konsolerc

%find_lang konsole --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konsole.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif


%files -f konsole.lang
%doc README*
%{_kf6_bindir}/konsole
%{_kf6_bindir}/konsoleprofile
%{_kf6_datadir}/applications/org.kde.konsole.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_kf6_datadir}/kio/servicemenus/konsolerun.desktop
%{_kf6_datadir}/knotifications6/konsole.notifyrc
%{_kf6_datadir}/qlogging-categories6/konsole.*
%{_kf6_datadir}/zsh/site-functions/_konsole
%{_kf6_metainfodir}/org.kde.konsole.appdata.xml
%if 0%{?flatpak}
%{_kf6_datadir}/icons/hicolor/*/apps/utilities-terminal.*
%endif


%files part
%config(noreplace) %{_kf6_sysconfdir}/xdg/konsolerc
%{_kf6_libdir}/libkonsoleapp.so.*
%{_kf6_libdir}/libkonsoleprivate.so.*
%{_kf6_qtplugindir}/konsoleplugins/
%{_kf6_qtplugindir}/kf6/parts/konsolepart.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
