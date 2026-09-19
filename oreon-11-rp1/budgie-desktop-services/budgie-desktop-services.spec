%global source0_hash 2304b2958abde6b75af678f1fd523ee6afba84c1f54d20c6eb4738415fffb799

Name:    budgie-desktop-services
Version: 1.0.2
Release: 1%{?dist}
Summary: Daemon responsible for enabling various features of Budgie Desktop

License: MPL-2.0
URL:     https://forge.moderndesktop.dev/BuddiesOfBudgie/budgie-desktop-services
Source0: %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: cmake(KWayland)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(toml11)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros

%description
The future central hub and orchestrator for Budgie Desktop 
(with a focus on Budgie 11). Today, it primarily provides Wayland-native 
display configuration for Budgie 10.10; over time it will coordinate broader 
desktop logic for Budgie 11.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%files
%license COPYING
%{_bindir}/org.buddiesofbudgie.Services
%{_datadir}/dbus-1/system.d/org.buddiesofbudgie.Services.conf

%changelog
%autochangelog
