%global source0_hash c2c7b782659b23e844d7277070a94e396ff547bde438c084e3a3297e853567f4
%global source1_hash 2ad745b42c0a52e539a6afe2c571e27ea7c5ce407f096ec2bfc3dad6795a4bcd
Name:           cockpit-machines
Version:        357
Release:        1%{?dist}
Summary:        Cockpit user interface for virtual machines
License:        LGPL-2.1-or-later AND MIT
URL:            https://github.com/cockpit-project/cockpit-machines
Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-node-%{version}.tar.xz
BuildArch:      noarch
%if 0%{?suse_version}
%else
%endif
%if %{defined rebuild_bundle}
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
Requires: qemu-kvm-core
Recommends: qemu-block-curl
Recommends: qemu-char-spice
Recommends: qemu-device-usb-host
Recommends: qemu-device-usb-redirect
%endif
Requires: libvirt-client
Requires: libvirt-dbus >= 1.2.0
Requires: virt-install >= 3.0.0
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
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  nodejs-esbuild
# /oreon:deps
%description
Cockpit component for managing libvirt virtual machines.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}
%if %{defined rebuild_bundle}
%setup -q -D -T -a 1 -n %{name}
%endif

%build

%if %{defined rebuild_bundle}
rm -rf dist
NODE_ENV=production NODE_PATH=/usr/lib/node_modules:$(echo /usr/lib/node_modules_*) ./build.js
%else
%endif
%install
%make_install PREFIX=/usr
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
