%global source0_hash 0d11f41d489f32303988e5a2eee8cef7f4eb18faea5614e65bf202007ea21dd5
%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%global base_name    libkscreen
Name:    libkscreen-qt5
Summary:        KDE display configuration library
Version: 5.27.11
Release:        6%{?dist}
License: GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{base_name}
%global revision %(echo %{version} | cut -d. -f3)
%if "%{revision}" >= "50"
%global stable_kf5 unstable
%else
%global stable_kf5 stable
%endif
Source0:        https://download.kde.org/stable/plasma/%{version}/%{base_name}-%{version}.tar.xz
Patch1:  libkscreen-5.6.4-rhel-nowayland.patch
%global __provides_exclude_from ^(%{_kf5_plugindir}/.*\\.so)$
Requires:       kf5-filesystem
Provides:       kf5-kscreen%{?_isa} = %{version}-%{release}
Provides:       kf5-kscreen = %{version}-%{release}
Obsoletes:      kf5-kscreen <= 1:5.2.0
%if %{with kf6_compat}
Requires:       libkscreen
%endif
# oreon:deps
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libxcb-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtwayland-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  wayland-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n libkscreen-qt5-devel -f %{oreon_filedir}/libkscreen-qt5-devel.list

%changelog

%autochangelog
