%global source0_hash 21b61ca4a29f49c2ab717624605e9dbe0abd8054aac2fd26098492f29c871cfa
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:           kweather
Version:        26.08.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
Summary:        Convergent KDE weather application
Url:            https://apps.kde.org/kweather/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       kf6-kcoreaddons%{?_isa}
Requires:       kf6-kholidays%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       qt6-qtcharts%{?_isa}
Recommends:     (%{name}-plasma-applet%{?_isa} = %{version}-%{release} if plasma-workspace)
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KWeatherCore)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-krunner-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Weather application for Plasma Mobile

%package plasma-applet
Summary:        Plasma weather applet
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       libplasma%{?_isa}
%description plasma-applet
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
chmod -x %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstreamcli validate --no-net %{buildroot}%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n kweather-plasma-applet -f %{oreon_filedir}/kweather-plasma-applet.list

%changelog

%autochangelog
