%global source0_hash 0d11f41d489f32303988e5a2eee8cef7f4eb18faea5614e65bf202007ea21dd5

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]

%global base_name    libkscreen

Name:    libkscreen-qt5
Summary: KDE display configuration library
Version: 5.27.11
Release: 6%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{base_name}

Source0: https://download.kde.org/%{stable_kf5}/plasma/%{version}/%{base_name}-%{version}.tar.xz

Patch1:  libkscreen-5.6.4-rhel-nowayland.patch

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5Config)
BuildRequires:  kf5-rpm-macros
BuildRequires:  systemd-rpm-macros
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:  kf5-kwayland-devel >= 5.22
%endif
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  wayland-devel

BuildRequires:  cmake(Qt5LinguistTools)

Requires:       kf5-filesystem

Provides:       kf5-kscreen%{?_isa} = %{version}-%{release}
Provides:       kf5-kscreen = %{version}-%{release}
Obsoletes:      kf5-kscreen <= 1:5.2.0

%if %{with kf6_compat}
# Install the KF6 service
Requires:       libkscreen
%endif

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kf5-kscreen-devel = %{version}-%{release}
Provides:       kf5-kscreen-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kf5-kscreen-devel <= 1:5.2.0
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{base_name}-%{version}

%if 0%{?rhel} && 0%{?rhel} <= 7
%patch -P1 -p1 -b .nowayland
%endif

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang_kf5 libkscreen5_qt

%if %{with kf6_compat}
rm -rf %{buildroot}%{_datadir}/dbus-1/
rm -rf %{buildroot}%{_userunitdir}/
rm -rf %{buildroot}%{_kf5_bindir}/
rm -rf %{buildroot}%{_kf5_libexecdir}/
rm -rf %{buildroot}%{_kf5_datadir}/zsh
%endif

%files -f libkscreen5_qt.lang
%license LICENSES/*
%{_kf5_libdir}/libKF5Screen.so.5.*
%{_kf5_libdir}/libKF5Screen.so.8*
%{_kf5_libdir}/libKF5ScreenDpms.so.5.*
%{_kf5_libdir}/libKF5ScreenDpms.so.8*
%{_kf5_plugindir}/kscreen/
%{_kf5_datadir}/qlogging-categories5/libkscreen.categories
%if %{without kf6_compat}
%{_kf5_bindir}/kscreen-doctor
%{_kf5_libexecdir}/kscreen_backend_launcher
%{_datadir}/dbus-1/services/org.kde.kscreen.service
%{_kf5_datadir}/zsh/site-functions/_kscreen-doctor
%{_userunitdir}/plasma-kscreen.service
%endif

%files devel
%{_kf5_includedir}/KScreen/
%{_kf5_includedir}/kscreen_version.h
%{_kf5_libdir}/libKF5Screen.so
%{_kf5_libdir}/libKF5ScreenDpms.so
%{_kf5_libdir}/cmake/KF5Screen/
%{_libdir}/pkgconfig/kscreen2.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KScreen.pri

%changelog
%autochangelog
