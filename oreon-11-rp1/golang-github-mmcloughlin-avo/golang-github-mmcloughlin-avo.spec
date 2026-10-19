%global source0_hash 990471970acb01356b3cf7c22fd5c2707262bfa6e5c91f2e331d9dd0ab1f5743
%ifarch x86_64
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/mmcloughlin/avo
Version:                0.6.0
%gometa -L
%global common_description %{expand:
Generate x86 Assembly with Go.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           golang-github-mmcloughlin-avo
Release:        1%{?dist}
Summary:        Generate x86 Assembly with Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/avo-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d gotypes
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
