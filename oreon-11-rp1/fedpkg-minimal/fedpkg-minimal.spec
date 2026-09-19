%global source0_hash 9138b74d806d772d56fcce274dcdaa22e3c26e272195579c076fb6a9004b8ce4

Name:           fedpkg-minimal
Version:        1.2.0
Release:        17%{?dist}
Summary:        Script to allow fedpkg fetch to work

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://pagure.io/%{name}
Source0:        https://releases.pagure.org/%{name}/%{name}-%{version}.tar.gz
Patch1:         0001-curl-max-time-in-seconds-not-minutes.patch
Patch2:         0002-Add-Accept-Encoding-identity-header-to-curl-requests.patch
Patch3:         0003-Add-Accept-Encoding-identity-header-to-curl-requests-tests.patch

BuildArch:      noarch

Requires:       curl

Conflicts:      fedpkg

%description
Script for use in Koji to allow sources to be fetched

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%install
install -d %{buildroot}%{_bindir}
install -pm 755 bin/fedpkg %{buildroot}%{_bindir}/fedpkg
install -pm 755 bin/fedpkg-stg %{buildroot}%{_bindir}/fedpkg-stg
install -pm 755 bin/fedpkg-base %{buildroot}%{_bindir}/fedpkg-base

%check
./tests/run-tests.sh

%files
%doc README.md AUTHORS.md
%license LICENSE
%{_bindir}/fedpkg
%{_bindir}/fedpkg-stg
%{_bindir}/fedpkg-base

%changelog
%autochangelog
