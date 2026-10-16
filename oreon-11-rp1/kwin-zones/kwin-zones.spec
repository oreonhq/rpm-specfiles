%global source0_hash eca1591c33d37a8fc97a4729ad4ec905055d2d8774feccbfe4078392ac1ae711

Name:          kwin-zones
Version:       1.0.12
Release:       1%{?dist}
Summary:       Wayland ext-zones for KWin

License:       BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND MIT
URL:           https://invent.kde.org/automotive/%{name}

Source:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

# https://invent.kde.org/automotive/kwin-zones/-/merge_requests/5

# https://invent.kde.org/automotive/kwin-zones/-/merge_requests/6

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(qt6waylandscannertools)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(libdrm)
BuildRequires: cmake(Qt6GuiPrivate)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KWin)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license LICENSES/*
%doc README.md
%{_kf6_qtplugindir}/kwin/plugins/KWinZones.so
%{_kf6_qmldir}/org/kde/zones/

%changelog
%autochangelog
