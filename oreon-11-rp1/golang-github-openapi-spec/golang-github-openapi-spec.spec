%global source0_hash bca84803dcca97ce10f225ea1a5d88d2cbcfc3ad914160cf058ce264e4de381f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/spec
Version:                0.20.0
%gometa
%global common_description %{expand:
The object model for OpenAPI specification documents.
Currently supports Swagger 2.0.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Openapi specification object model
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/spec-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-openapi/jsonpointer)
BuildRequires:  golang(github.com/go-openapi/jsonreference)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(gopkg.in/yaml.v2)
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
