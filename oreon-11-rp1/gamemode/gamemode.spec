%global source0_hash 98cd1bcf6101c92fe87f974c7776af23c7e18f29ce6ecfe572b1c39dcde5c181
Name:		gamemode
Version:	1.8.2
Release:        1%{?dist}
Summary:        Optimize system performance for games on demand
License:	BSD-3-Clause
URL:		https://github.com/FeralInteractive/gamemode
Source0:        https://github.com/FeralInteractive/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  polkit-devel
BuildRequires:  systemd
# /oreon:deps
%description
GameMode is a daemon/lib combo for GNU/Linux that allows games to
request a set of optimizations be temporarily applied to the host OS.
GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU "powersave" or "ondemand" governors, but is
now host to a range of optimisation features and configurations, like
tweaking various settings: the CPU govenor, the I/O priority, the
kernel scheduler, the GPU performance mode and gpu overclocking
(NVIDIA). It can also excute custom scripts when launching games.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%check

%meson_test
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gamemode-devel -f %{oreon_filedir}/gamemode-devel.list

%changelog

%autochangelog
