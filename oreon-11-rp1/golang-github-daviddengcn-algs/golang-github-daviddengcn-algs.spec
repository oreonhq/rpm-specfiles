%global source0_hash e07339c2778175fd898751cccf70b5794e7e89c05f83ee9dc9d1f7f030877019
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/daviddengcn/go-algs
%global commit          fe23fabd9d0670e4675326040ba7c285c7117b4c
%gometa
%global common_description %{expand:
Some algorithms in go: maxflow(min-cuts or graph-cuts), edit-distance.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Maxflow and edit-distance algorithms in Go
License:        BSD-2-Clause-Views
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-algs-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golangplus/testing/assert)
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
