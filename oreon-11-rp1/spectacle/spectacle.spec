%global source1_hash 276484e970040e4cb2d71e70ac22f8f00f7a81607596dfbd6ef00cb83e1e9c28
%global source0_hash 4ee7cf93305fcc831d5983b173cfa06582c5b3c2180c5c9be83f1653c66ac6cf
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif
ExcludeArch: %{ix86}
Name:    spectacle
Summary:        Screenshot capture utility
Epoch:   1
Version:        24.12.3
Release:        1%{?dist}
License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/spectacle/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
%global majmin %(echo %{version} | cut -d. -f1,2)
Recommends:     qt6-qtimageformats%{?_isa}
Requires:       tesseract
Conflicts: kde-l10n < 17.03
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPipeWire)
BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(OpenCV)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QWebpPlugin)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(ZXing)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.spectacle.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
