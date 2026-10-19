%global source0_hash 330fef440ffeb842a7dcfffc8303743f1feae83e8d6131078b5a44ff11bc3850
Name:           R-pkgconfig
Version:        %R_rpm_version 2.0.3
Release:        1%{?dist}
Summary:        Private Configuration for 'R' Packages
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=pkgconfig&version=%{version}#/pkgconfig_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Set configuration options on a per-package basis. Options set by a given
package only apply to that package, other packages are unaffected.

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
