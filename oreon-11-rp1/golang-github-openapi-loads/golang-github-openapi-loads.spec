%global source0_hash 9b7f7e099d6b3e343c96cd02a2ab52dce5588921889bb2d285caf08f24b5f645
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/loads
Version:                0.25.3
%gometa
%global common_description %{expand:
Loading of OAI specification documents from local or remote locations. Supports
JSON and YAML documents.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Openapi specification object model
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/loads-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-openapi/analysis)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/swag)
BuildRequires:  golang(github.com/go-openapi/validate)
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
