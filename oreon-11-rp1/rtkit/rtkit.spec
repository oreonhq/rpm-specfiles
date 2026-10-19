%global source0_hash bd6c1a236e479c59658b1e7be072e5990ad97439a2ecac433b0edfeb2531b52c
Name:             rtkit
Version:          0.14
Release:        1%{?dist}
Summary:        Realtime Policy and Watchdog Daemon
License:          GPL-3.0-or-later AND MIT
%define forgeurl https://gitlab.freedesktop.org/pipewire/rtkit
%define tag v%{version}
%forgemeta
URL:              %{forgeurl}
Requires:         dbus
Requires:         polkit
Source0:        http://0pointer.de/public/%{name}-%{version}.tar.xz
Patch:            remove-debug-messages.patch
# oreon:deps
BuildRequires:  dbus-devel
BuildRequires:  gcc
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  polkit-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xxd
# /oreon:deps
%description
RealtimeKit is a D-Bus system service that changes the
scheduling policy of user processes/threads to SCHED_RR (i.e. realtime
scheduling mode) on request. It is intended to be used as a secure
mechanism to allow real-time scheduling to be used by normal user
processes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir rtkit-v%{version}
%oreon_prep
%build

%meson \
  -D systemd_systemunitdir=%{_unitdir}			\
  -D installed_tests=false				\
  %{nil}
%meson_build
%{_vpath_builddir}/rtkit-daemon --introspect >org.freedesktop.RealtimeKit1.xml
%install
install -Dm0644 org.freedesktop.RealtimeKit1.xml -t %{buildroot}%{_datadir}/dbus-1/interfaces/
%meson_install
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
%oreon_autofiles main

%post

%systemd_post rtkit-daemon.service
dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig >/dev/null 2>&1 || :
%preun

%systemd_preun rtkit-daemon.service
%postun

%systemd_postun_with_restart rtkit-daemon.service
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14-1
- Prepare for Oreon 11 (RP1)
