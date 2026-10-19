%global source0_hash c2aace3ac1a9c8c9b9c57ba0ffc99a3d310737cc004db0491802e03536e27c69
Name:    pulseaudio-qt
Summary:        Qt bindings for PulseAudio
Version: 1.9.0
Release:        1%{?dist}
License: CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/libraries/pulseaudio-qt
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse)
# /oreon:deps
%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package qt6
Summary: Qt6 bindings for PulseAudio
%description qt6
%{summary}.

%package qt6-devel
Summary: Development files for %{name} (Qt6)
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
%description qt6-devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_kf6_includedir}/pulseaudioqt_version.h
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pulseaudio-qt-qt6 -f %{oreon_filedir}/pulseaudio-qt-qt6.list
%files -n pulseaudio-qt-qt6-devel -f %{oreon_filedir}/pulseaudio-qt-qt6-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.1-1
- Import
