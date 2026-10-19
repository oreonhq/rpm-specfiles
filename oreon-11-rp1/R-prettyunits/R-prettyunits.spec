%global source0_hash f059f27e2a5c82e351fe05b87ad712f7afc273c651450453f59d99af5deeacea
Name:           R-prettyunits
Version:        %R_rpm_version 1.2.0
Release:        1%{?dist}
Summary:        Pretty, Human Readable Formatting of Quantities
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=prettyunits&version=%{version}#/prettyunits_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Pretty, human readable formatting of quantities.
Time intervals: 1337000 -> 15d 11h 23m 20s.
Vague time intervals: 2674000 -> about a month ago.
Bytes: 1337 -> 1.34 kB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
