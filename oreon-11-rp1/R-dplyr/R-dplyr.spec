%global source0_hash cf730414d5d4ab387b4e9890a4b1df9d17a3903488e8da8df1cf2e11e44558cb
Name:           R-dplyr
Version:        %R_rpm_version 1.1.4
Release:        1%{?dist}
Summary:        A Grammar of Data Manipulation
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=dplyr&version=%{version}#/dplyr_%{version}.tar.gz
ExcludeArch:    %{ix86}
Obsoletes:      %{name}-devel < 0.8.5-4
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A fast, consistent tool for working with data frame like objects, both in
memory and out of memory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%install
%R_install
%R_save_files
%oreon_autofiles main

%check

%R_check \--no-examples
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
