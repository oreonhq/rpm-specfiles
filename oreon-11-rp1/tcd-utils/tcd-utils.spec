%global source0_hash 3e231a223b66299fd37c38c063f1fa5b152b4793fc157d4fb478a6ee54f2aa68
Name:		tcd-utils
Version:	20240222
Release:        1%{?dist}
Summary:        TCD (Tide Constituent Database) Utils
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.flaterco.com/xtide/
Source0:        https://flaterco.com/files/xtide/tcd-utils-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libtcd-devel
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
