%global source0_hash 3d1e92a9206811ad128b28795d20a0d31da5f0c29ea7f1caaf1194ed3e49765f
Name:           R-microbenchmark
Version:        %R_rpm_version 1.5.0
Release:        1%{?dist}
Summary:        Accurate Timing Functions
License:        BSD-2-Clause
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=microbenchmark&version=%{version}#/microbenchmark_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
Provides infrastructure to accurately measure and compare the execution
time of R expressions.

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
