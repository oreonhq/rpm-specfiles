%global source0_hash 4181f7334e032ae0775c5dec49d6137eb25d5430ca3792d321793307b3dda38f
Name:           R-brew
Version:        %R_rpm_version 1.0-10
Release:        1%{?dist}
Summary:        Templating Framework for Report Generation
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=brew&version=1.0-10#/brew_1.0-10.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
brew implements a templating framework for mixing text and R code for
report generation. brew template syntax is similar to PHP, Ruby's erb
module, Java Server Pages, and Python's psp module.

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
