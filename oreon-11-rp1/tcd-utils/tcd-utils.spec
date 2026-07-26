%global source0_hash 3e231a223b66299fd37c38c063f1fa5b152b4793fc157d4fb478a6ee54f2aa68

Name:		tcd-utils
Version:	20240222
Release:	6%{?dist}
Summary:	TCD (Tide Constituent Database) Utils

# https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/551
# SPDX confirmed
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.flaterco.com/xtide/
Source0:	https://flaterco.com/files/xtide/tcd-utils-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:	libtcd-devel

%description
TCD Utils includes:
* build_tide_db to convert harmonics.txt, offsets.xml, and NAVO
  formats to harmonics.tcd;
* restore_tide_db to generate harmonics.txt and offsets.xml from
  harmonics.tcd

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
%make_build

%install
%make_install
 
%files
%license COPYING
%doc ChangeLog
%doc README
%{_bindir}/*

%changelog
%autochangelog
