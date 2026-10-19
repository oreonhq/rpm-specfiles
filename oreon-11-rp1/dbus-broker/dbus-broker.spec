%global source0_hash f819a8db8795fa08c767612e3823fd594694a0990f2543ecf35d6a1a6bf2ab5b
%global dbus_user_id 81
Name:                 dbus-broker
Version:              37
Release:        1%{?dist}
Summary:        Linux D-Bus Message Broker
License:              Apache-2.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND (Apache-2.0 OR LGPL-2.1-or-later)
URL:                  https://github.com/bus1/dbus-broker
Source0:        https://github.com/bus1/dbus-broker/releases/download/v%{version}/dbus-broker-%{version}.tar.xz
Patch0:               0001-test-sockopt-loosen-verification-of-stale-pidfds.patch
Requires:             dbus-common
# oreon:deps
BuildRequires:  bindgen-cli
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  jq
BuildRequires:  meson
BuildRequires:  pkgconfig(audit)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-docutils
BuildRequires:  rust
# /oreon:deps
%description
dbus-broker is an implementation of a message bus as defined by the D-Bus
specification. Its aim is to provide high performance and reliability, while
keeping compatibility to the D-Bus reference implementation. It is exclusively
written for Linux systems, and makes use of many modern features provided by
recent Linux kernel releases.

%package tests
Summary:              Internal unit and reference tests of dbus-broker
Requires:             %{name}%{_isa} = %{version}-%{release}
%description tests
dbus-broker's unit and reference tests that can be used to verify the functionality
of the installed dbus-broker.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Create a sysusers.d config file
cat >dbus-broker.sysusers.conf <<EOF
u dbus %{dbus_user_id} 'System Message Bus' - -
EOF

%build

%meson -Dselinux=true -Daudit=true -Ddocs=true -Dtests=true -Dsystem-console-users=gdm -Dlinux-4-17=true
%meson_build
%install
%meson_install
install -m0644 -D dbus-broker.sysusers.conf %{buildroot}%{_sysusersdir}/dbus-broker.conf
rm -f %{buildroot}%{_bindir}/dbus-broker-session
rm -f %{buildroot}%{_journalcatalogdir}/dbus-broker-session.catalog
rm -f %{buildroot}%{_mandir}/man1/dbus-broker-session.1*
%oreon_autofiles dbus-broker-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%post

%systemd_post dbus-broker.service
%systemd_user_post dbus-broker.service
%journal_catalog_update
%preun

%systemd_preun dbus-broker.service
%systemd_user_preun dbus-broker.service
%postun

%systemd_postun dbus-broker.service
%systemd_user_postun dbus-broker.service
%triggerpostun -- dbus-daemon

if [ $2 -eq 0 ] && [ -x /usr/bin/systemctl ] ; then
        systemctl --no-reload          preset dbus-broker.service || :
        systemctl --no-reload --global preset dbus-broker.service || :
fi
%files -f %{oreon_filedir}/main.list
%files -n dbus-broker-tests -f %{oreon_filedir}/dbus-broker-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 37-1
- Prepare for Oreon 11 (RP1)
