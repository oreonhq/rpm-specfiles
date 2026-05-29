%global source0_hash 538a39ebbd4b2a85a38cc90f408759c32986a85b7cf48c936d6bce32bd9cd341
%global source1_hash 447a260efffc3ed8c6a710dbcb2b6bb52071b1d42ab3e0c74ac779cfad303997

# SPDX-License-Identifier: LGPL-2.1-or-later
#
# Copyright (C) 2017-2020 Red Hat, Inc.

Name:           cockpit-podman
Version:        122
Release:        1%{?dist}
Summary:        Cockpit component for Podman containers
License:        LGPL-2.1-or-later
URL:            https://github.com/cockpit-project/cockpit-podman

# distributions which ship nodejs-esbuild can rebuild the bundle during package build
%if 0%{?fedora} >= 42
%define rebuild_bundle 1
%endif

Source0:        https://github.com/cockpit-project/cockpit-podman/releases/download/122/cockpit-podman-122.tar.xz
Source1:        https://github.com/cockpit-project/cockpit-podman/releases/download/122/cockpit-podman-node-122.tar.xz

BuildArch:      noarch
%if 0%{?suse_version}
# Suse's package has a different name
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

Requires:       cockpit-bridge
Requires:       podman >= 2.0.4
# HACK https://github.com/containers/crun/issues/1091
%if 0%{?centos} == 9
Requires:       criu-libs
%elif 0%{?suse_version}
Requires:       libcriu2
%endif

Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(@xterm/addon-webgl)) = 0.19.0
Provides: bundled(npm(@xterm/xterm)) = 6.0.0
Provides: bundled(npm(docker-names)) = 1.2.1
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
The Cockpit user interface for Podman containers.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 122-1
- Prepare for Oreon 11 (RP1)
