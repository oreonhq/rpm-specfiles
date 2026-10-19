%global source0_hash 74cd7e55f2a0a72a8211043122bdaaf1d15fe8393466baa57b593feb3ae1fd04
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    krdc
Summary:        Remote desktop client
Version: 26.04.3
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/network/krdc
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  (cmake(FreeRDP) >= 3.00 with cmake(FreeRDP) < 4)
BuildRequires:  (cmake(FreeRDP-Client) >= 3.00 with cmake(FreeRDP-Client) < 4)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(WinPR)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  freerdp
BuildRequires:  fuse3-devel
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libvncserver-devel
BuildRequires:  oxygen-icon-theme
BuildRequires:  pkgconfig(libssh)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir krdc-%{version}
%oreon_prep
%build

%cmake_kf6 \
	-DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
mkdir -p %{buildroot}%{_datadir}/icons/hicolor
pushd %{_datadir}/icons/oxygen/
for icon in $(find */apps -name krdc.*) $(find base/*/apps -name krdc.*); do
cp -v --parents -n ${icon} %{buildroot}%{_datadir}/icons/hicolor/
done
mv %{buildroot}%{_datadir}/icons/hicolor/base/* %{buildroot}%{_datadir}/icons/hicolor/ ||:
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n krdc-libs -f %{oreon_filedir}/krdc-libs.list
%files -n krdc-devel -f %{oreon_filedir}/krdc-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
