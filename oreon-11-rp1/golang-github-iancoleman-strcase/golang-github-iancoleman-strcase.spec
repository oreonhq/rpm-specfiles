%global source0_hash 1cd6a7584be53d74b1e3014fa7d50a998b330580ec13109cd0558f554d3457e9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/iancoleman/strcase
Version:                0.3.0
%gometa
%global common_description %{expand:
A Golang package for converting to snake_case or CamelCase.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A Golang package for converting to snake_case or CamelCase
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/strcase-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
