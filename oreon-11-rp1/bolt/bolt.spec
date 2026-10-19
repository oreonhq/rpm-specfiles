%global source0_hash 3e23e862bf798476379bd4749824ed763a97ea7ee20f750a3ad03669994b34c9
Name:          bolt
Version:       0.9.11
Release:        1%{?dist}
Summary:        Thunderbolt device manager
License:       LGPL-2.1-or-later
URL:           https://gitlab.freedesktop.org/bolt/bolt
Source0:        https://gitlab.freedesktop.org/bolt/bolt/-/archive/0.9.11/bolt-0.9.10.tar.gz
Patch0:        0001-test-test-unix-skip-unix-domain-socket-test.patch
%{?systemd_requires}
# oreon:deps
BuildRequires:  /usr/bin/dbus-daemon
BuildRequires:  asciidoc
BuildRequires:  dbus
BuildRequires:  gcc
BuildRequires:  libudev-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  polkit-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-dbusmock
BuildRequires:  python3-gobject-base
BuildRequires:  systemd
BuildRequires:  umockdev-devel
# /oreon:deps
%description
bolt is a system daemon to manage Thunderbolt devices via a D-BUS
API. Thunderbolt 3 introduced different security modes that require
devices to be authorized before they can be used. The D-Bus API can be
used to list devices, enroll them (authorize and store them in the
local database) and forget them again (remove previously enrolled
devices). It also emits signals if new devices are connected (or
removed). During enrollment devices can be set to be automatically
authorized as soon as they are connected.  A command line tool, called
boltctl, can be used to control the daemon and perform all the above
mentioned tasks.

%package tests
Summary: Test files for bolt
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
Test files for bolt

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir bolt-%{version}-9d1d66380353dab94c28466f34adb2ba6c7e4393
%oreon_prep
%build

sed -i "s/WatchdogSec=3min/#WatchdogSec=3min/g" data/bolt.service.in
%meson -Ddb-name=boltd -Dinstall-tests=true
%meson_build
%check

%meson_test
%install
%meson_install
%oreon_autofiles bolt-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list
%files -n bolt-tests -f %{oreon_filedir}/bolt-tests.list

%changelog

%autochangelog
