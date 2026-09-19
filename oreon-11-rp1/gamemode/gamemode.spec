%global source0_hash 98cd1bcf6101c92fe87f974c7776af23c7e18f29ce6ecfe572b1c39dcde5c181

Name:		gamemode
Version:	1.8.2
Release:	4%{?dist}
Summary:	Optimize system performance for games on demand
License:	BSD-3-Clause
URL:		https://github.com/FeralInteractive/gamemode
Source0:	%{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: asciidoc
BuildRequires: meson
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(inih) >= 49
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: polkit-devel
BuildRequires: systemd

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

%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%files
%license LICENSE.txt
%doc	 README.md
%{_bindir}/gamemoded
%{_bindir}/gamemodelist
%{_bindir}/gamemoderun
%{_bindir}/gamemode-simulate-game
%{_libexecdir}/cpucorectl
%{_libexecdir}/cpugovctl
%{_libexecdir}/gpuclockctl
%{_libexecdir}/procsysctl
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_datadir}/polkit-1/rules.d/gamemode.rules
%{_datadir}/gamemode/gamemode.ini
%{_libdir}/libgamemode*.so.*
%{_sysusersdir}/gamemode.conf
%{_userunitdir}/gamemoded.service
%{_mandir}/man8/gamemoded.8*
%{_mandir}/man1/gamemoderun.1*
%{_mandir}/man1/gamemodelist.1*
%{_mandir}/man1/gamemode-simulate-game.1*
%{_metainfodir}/io.github.feralinteractive.gamemode.metainfo.xml
%config(noreplace) %{_sysconfdir}/security/limits.d/10-gamemode.conf

%files devel
%{_includedir}/gamemode_client.h
%{_libdir}/pkgconfig/gamemode*.pc
%{_libdir}/pkgconfig/libgamemodeauto.pc
%{_libdir}/libgamemode*.so

%changelog
%autochangelog
