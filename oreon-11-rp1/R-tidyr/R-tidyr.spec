%global source0_hash 04c0e6daf0af682af73763a42c027d7171761cdbdbf9ff7a77a0e421343d665a
Name:           R-tidyr
Version:        %R_rpm_version 1.3.2
Release:        1%{?dist}
Summary:        Tidy Messy Data
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=tidyr&version=%{version}#/tidyr_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Tools to help to create tidy data, where each column is a variable, each
row is an observation, and each cell contains a single value.  'tidyr'
contains tools for changing the shape (pivoting) and hierarchy (nesting and
'unnesting') of a dataset, turning deeply nested lists into rectangular
data frames ('rectangling'), and extracting values out of string columns.
It also includes tools for working with missing values (both implicit and
explicit).

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
