Name: cockpit-files
Version: 37
Release: 1%{?dist}
Summary: A filesystem browser for Cockpit
License: LGPL-2.1-or-later

# distributions which ship nodejs-esbuild can rebuild the bundle during package build
%if 0%{?fedora} >= 42
%define rebuild_bundle 1
%endif

Source0: https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1: https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-node-%{version}.tar.xz

BuildArch: noarch
BuildRequires: make
%if 0%{?suse_version}
# Suse's package has a different name
BuildRequires:  appstream-glib
%else
BuildRequires:  libappstream-glib
%endif
BuildRequires: gettext
%if %{defined rebuild_bundle}
BuildRequires: /usr/bin/node
BuildRequires: nodejs-esbuild
%endif

Requires: cockpit-bridge >= 318

# Replace the older cockpit-navigator provided by 45Drives
Obsoletes: cockpit-navigator < 0.5.11

Provides: bundled(npm(@patternfly/patternfly)) = 6.4.0
Provides: bundled(npm(@patternfly/react-core)) = 6.4.1
Provides: bundled(npm(@patternfly/react-icons)) = 6.4.0
Provides: bundled(npm(@patternfly/react-styles)) = 6.4.0
Provides: bundled(npm(@patternfly/react-table)) = 6.4.1
Provides: bundled(npm(@patternfly/react-tokens)) = 6.4.0
Provides: bundled(npm(dequal)) = 2.0.3
Provides: bundled(npm(focus-trap)) = 7.6.4
Provides: bundled(npm(lodash)) = 4.17.23
Provides: bundled(npm(prop-types)) = 15.8.1
Provides: bundled(npm(react)) = 18.3.1
Provides: bundled(npm(react-dom)) = 18.3.1
Provides: bundled(npm(scheduler)) = 0.23.2
Provides: bundled(npm(tabbable)) = 6.4.0
Provides: bundled(npm(throttle-debounce)) = 5.0.2
Provides: bundled(npm(tslib)) = 2.8.1

%description
A filesystem browser for Cockpit

%prep
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

# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

# this can't be meaningfully tested during package build; tests happen through
# FMF (see plans/all.fmf) during package gating

%files
%doc README.md
%license LICENSE dist/index.js.LEGAL.txt
%{_datadir}/cockpit/*
%{_datadir}/metainfo/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 37-1
- Prepare for Oreon 11 (RP1)
