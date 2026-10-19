%global source0_hash c86f364ba899b8662f5da3e1a75f43ae081ab04e0d51171d052356e7ee4b72a0
Name:           R-glue
Version:        %R_rpm_version 1.8.0
Release:        1%{?dist}
Summary:        Interpreted String Literals
License:        MIT
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=glue&version=%{version}#/glue_%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
An implementation of interpreted string literals, inspired by Python's
Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
Triple-Quoted String Literals
<https://docs.julialang.org/en/v1.3/manual/strings/#Triple-Quoted-String-Literals-1>.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
rm -f glue/tests/testthat/test-vctrs.R # unconditional suggest, should be fixed

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
