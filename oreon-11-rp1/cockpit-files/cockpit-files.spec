%global source0_hash cb4a7746b240148716e18d9fea42a5a4602155377a609765efc993651e691802
%global source1_hash 050e9acf1844695345603e4c1bdabf422eb6371aeea15c3f4561653ddc92f429
Name: cockpit-files
Version: 45
Release:        1%{?dist}
Summary:        A filesystem browser for Cockpit
License: LGPL-2.1-or-later
Source0:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/cockpit-project/%{name}/releases/download/%{version}/%{name}-node-%{version}.tar.xz
BuildArch: noarch
%if 0%{?suse_version}
%else
%endif
%if %{defined rebuild_bundle}
%endif
Requires: cockpit-bridge >= 318
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
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  nodejs-esbuild
# /oreon:deps
%description
A filesystem browser for Cockpit

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
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
