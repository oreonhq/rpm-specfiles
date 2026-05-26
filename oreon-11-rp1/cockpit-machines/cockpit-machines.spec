# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 130c3639ed6b44f14f79b497cadd35c178761d1e70dc6bb1afeb35fac466424d
%global source1_sha256 2e0bfb252887f0d6fb8a0a5651f4b976620ddf45921c2e58d1390ccb51fe694a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# SPDX-License-Identifier: LGPL-2.1-or-later
#
# Copyright (C) 2021 Red Hat, Inc.

Name:           cockpit-machines
Version:        349.1
Release:        1%{?dist}
Summary:        Cockpit user interface for virtual machines
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/cockpit-project/cockpit-machines

# distributions which ship nodejs-esbuild can rebuild the bundle during package build
%if 0%{?fedora} >= 42
%define rebuild_bundle 1
%endif

Source0: https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1: https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-node-%{version}.tar.xz

BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires:  make
BuildRequires: gettext
%if 0%{?rhel} && 0%{?rhel} <= 8
BuildRequires: libappstream-glib-devel
%endif
%if %{defined rebuild_bundle}
BuildRequires: /usr/bin/node
BuildRequires: nodejs-esbuild
%endif

Requires: cockpit-bridge >= 215
%if 0%{?suse_version}
Requires: libvirt-daemon-qemu
%else
Requires: libvirt-daemon-driver-qemu
Requires: libvirt-daemon-driver-network
Requires: libvirt-daemon-driver-nodedev
Requires: libvirt-daemon-driver-storage-core
Requires: libvirt-daemon-config-network
Recommends: libvirt-daemon-driver-storage-disk
%if 0%{?rhel}
Requires: qemu-kvm
Suggests: qemu-kvm-block-curl
%else
# smaller footprint on Fedora, as qemu-kvm is really expensive on a server
Requires: qemu-kvm-core
Recommends: qemu-block-curl
Recommends: qemu-char-spice
Recommends: qemu-device-usb-host
Recommends: qemu-device-usb-redirect
# HACK: https://bugzilla.redhat.com/show_bug.cgi?id=2170110
%if 0%{?fedora} >= 38
Requires: (qemu-audio-spice if qemu-char-spice)
%endif
%endif
%endif
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0
Requires: virt-install >= 3.0.0
# Optional components
Recommends: libosinfo
Recommends: python3-gobject-base
Suggests: (qemu-virtiofsd or virtiofsd)

Provides: bundled(npm(@novnc/novnc)) = 1.5.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(@xterm/addon-webgl)) = 0.19.0
Provides: bundled(npm(@xterm/xterm)) = 6.0.0
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(ipaddr.js)) = 2.3.0
Provides: bundled(npm(lodash)) = 4.17.23
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1

%description
Cockpit component for managing libvirt virtual machines.

%prep
%oreon_verify_sources
%setup -q -n %{name}
%if %{defined rebuild_bundle}
%setup -q -D -T -a 1 -n %{name}
%endif

%build
%if %{defined rebuild_bundle}
rm -rf dist
# HACK: node module packaging is broken in Fedora ≤ 43; should be in
# common location, not major version specific one
NODE_ENV=production NODE_PATH=/usr/lib/node_modules:$(echo /usr/lib/node_modules_*) ./build.js
%else
# Use pre-built bundle on distributions without nodejs-esbuild
%endif

%install
%make_install PREFIX=/usr
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt dist/index.css.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

# The changelog is automatically generated and merged
%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 349.1-1
- Prepare for Oreon 11 (RP1)
