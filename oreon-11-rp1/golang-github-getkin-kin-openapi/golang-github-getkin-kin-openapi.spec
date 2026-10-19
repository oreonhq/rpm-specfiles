%global source0_hash 881d3a6f478b07bdd00939f5378908eab0223b1e9cfe2a8d75381d6681c3796b
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/getkin/kin-openapi
Version:                0.149.0
%gometa
%global common_description %{expand:
OpenAPI 3.0 (and Swagger v2) implementation for Go (parsing, converting,
validation, and more).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OpenAPI 3.0 (and Swagger v2) implementation for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/kin-openapi-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{with check}
%check

%gocheck \
	-d openapi3
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
