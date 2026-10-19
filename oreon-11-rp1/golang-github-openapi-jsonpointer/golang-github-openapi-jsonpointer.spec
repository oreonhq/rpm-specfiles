%global source0_hash 8d270abb12a9a7f84a775894a5d56ac24f9c2aaeb0dea91ef4ee5edb7519d7c8
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/jsonpointer
Version:                1.0.2
%gometa
%global common_description %{expand:
Fork of gojsonpointer with support for structs.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Gojsonpointer with support for structs
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jsonpointer-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
