%global source0_hash none

# 
ExcludeArch: %{ix86}

Name:    krdc
Summary: Remote desktop client
Version: 26.04.1
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/network/krdc
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: (cmake(FreeRDP) >= 3.00 with cmake(FreeRDP) < 4)
BuildRequires: (cmake(FreeRDP-Client) >= 3.00 with cmake(FreeRDP-Client) < 4)
BuildRequires: cmake(WinPR)
# winpr-makecert
BuildRequires: freerdp
BuildRequires: libvncserver-devel
BuildRequires: pkgconfig(libssh)
BuildRequires: fuse3-devel

# see icon hack in %%install
BuildRequires: oxygen-icon-theme

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html

# workaround https://bugs.kde.org/show_bug.cgi?id=365986
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
pushd %{_datadir}/icons/oxygen/
for icon in $(find */apps -name krdc.*) $(find base/*/apps -name krdc.*); do
cp -v --parents -n ${icon} %{buildroot}%{_datadir}/icons/hicolor/
done
mv %{buildroot}%{_datadir}/icons/hicolor/base/* %{buildroot}%{_datadir}/icons/hicolor/ ||:


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/krdc.categories
%{_kf6_bindir}/krdc
%{_kf6_datadir}/applications/org.kde.krdc.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/krdc.*
%{_kf6_datadir}/config.kcfg/krdc.kcfg
%{_kf6_datadir}/mime/packages/org.kde.krdc-mime.xml

%files libs
%{_kf6_libdir}/libkrdccore.so.5*
%{_kf6_libdir}/libkrdccore.so.%{version}
%{_kf6_qtplugindir}/krdc/

%files devel
%{_includedir}/krdc/
%{_includedir}/krdccore_export.h
%{_kf6_libdir}/libkrdccore.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
