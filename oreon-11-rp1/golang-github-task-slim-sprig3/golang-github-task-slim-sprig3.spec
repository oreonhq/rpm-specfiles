%global source0_hash 673b1acc819c60899e78b00f20da2b8270a0e370c01d3def9cda0a86167881fb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-task/slim-sprig/v3
Version:                3.0.0
%gometa -L -f
%global common_description %{expand:
Useful template functions for Go templates.}
%global golicenses      LICENSE.txt
%global godocs          docs CHANGELOG.md README.md
Name:           golang-github-task-slim-sprig3
Release:        1%{?dist}
Summary:        Useful template functions for Go templates
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/go-task/slim-sprig/archive/v%{version}/slim-sprig-%{version}.tar.gz
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

rm -vf network_test.go
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
