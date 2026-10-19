%global stable_kf6 stable
%global source0_hash 8660ad79c0d60fed77f29b36e1742841466af5405de702c81a121e6eeb625ebb
Name:           mpvqt
Version:        1.2.0
Release:        1%{?dist}
Summary:        QML wrapper for libmpv
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/libraries/mpvqt
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(mpv)
# /oreon:deps
%description
MpvQt is a libmpv wrapper for Qt Quick 2/Qml.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Quick)
Requires:       pkgconfig(mpv)
%description devel
Development headers and link library for building packages which use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mpvqt-devel -f %{oreon_filedir}/mpvqt-devel.list

%changelog

%autochangelog
