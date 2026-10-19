%global source0_hash 0e63ba2e1f624005fe25c67cdd403636a912e063d682eca07f2f1d65e9870d29
Name:           R-plogr
Version:        %R_rpm_version 0.2.0
Release:        1%{?dist}
Summary:        Devel files for R-plogr
Summary:        Devel files for R-plogr
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=plogr&version=%{version}#/plogr_%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      %{name}-devel <= 0.2.0
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A simple header-only logging library for C++. Add 'LinkingTo: plogr' to
'DESCRIPTION', and '#include <plogr.h>' in your C++ modules to use it.

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
