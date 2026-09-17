%global source0_hash ca36f6ddcf14ee4cb3ad5a850d444566a97ccb6762243f23a5f0448c9f8fc088

Name:           cockpit-image-builder
Version:        94
Release:        1%{?dist}
Summary:        Image builder plugin for Cockpit

License:        Apache-2.0
URL:            http://osbuild.org/
Source0:        https://github.com/osbuild/image-builder-frontend/releases/download/v%{version}/%{name}-%{version}.tar.gz

Obsoletes:      cockpit-composer < 54
Provides:       cockpit-composer = %{version}-%{release}

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  /usr/bin/node

Requires:       cockpit
Requires:       cockpit-files
Requires:       osbuild-composer >= 131

Recommends:     cockpit-machines

%description
The image-builder-frontend generates custom images suitable for
deploying systems or uploading to the cloud. It integrates into Cockpit
as a frontend for osbuild.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}

%build
# Nothing to build

%install
%make_install PREFIX=/usr
# drop source maps, they are large and just for debugging
find %{buildroot}%{_datadir}/cockpit/ -name '*.map' | xargs --no-run-if-empty rm --verbose

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*

%files
%doc cockpit/README.md
%license LICENSE
%{_datadir}/cockpit/cockpit-image-builder
%{_datadir}/metainfo/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 94-1
- Prepare for Oreon 11 (RP1)
