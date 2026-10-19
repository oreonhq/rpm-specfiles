%global source0_hash 62c6443cc44bfab705cba71a92b430bf11b45f8ffd35016a724b44ba805d2e93
%ifnarch %{ix86} %{arm}
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/go-openapi/swag
Version:                0.29.2
%gometa
%global common_description %{expand:
Contains a bunch of helper functions for go-openapi and go-swagger projects.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Goodie bag in use in the Go-openapi projects
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/swag-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/mailru/easyjson/jlexer)
BuildRequires:  golang(github.com/mailru/easyjson/jwriter)
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
