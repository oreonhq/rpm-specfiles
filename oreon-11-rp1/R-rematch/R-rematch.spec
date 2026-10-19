%global source0_hash 15daf7bf2907aef8503635bc8631fce9fd75248a1fc2496825588c4bdf785c26
Name:           R-rematch
Version:        %R_rpm_version 2.0.0
Release:        1%{?dist}
Summary:        Match Regular Expressions with a Nicer 'API'
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=rematch&version=%{version}#/rematch_%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A small wrapper on 'regexpr' to extract the matches and captured groups
from the match of a regular expression to a character vector.

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
