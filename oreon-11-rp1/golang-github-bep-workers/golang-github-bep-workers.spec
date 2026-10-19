%global source0_hash 3bea991d0f41147271dfb7a6470393ba046ecaa4e701d3779f235be7d5206152
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/bep/workers
Version:                1.1.0
%gometa
%global common_description %{expand:
Set up tasks to be executed in parallel.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Set up tasks to be executed in parallel
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/workers-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/frankban/quicktest)
BuildRequires:  golang(golang.org/x/sync/errgroup)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
