%global source0_hash e13106692c70b4b55898f82e8cf228d6c8523a5bbf79dba5d32e25408a841e25
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lestrrat-go/codegen
Version:                1.0.4
%gometa -f
%global common_description %{expand:
Utilities for generating Go code.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Utilities for generating Go code
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/codegen-%{version}.tar.gz
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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
