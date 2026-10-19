%global source0_hash 58bfadb198069425f8abe5dbddaf1f72b6c1ffb0debaa233a85b79f5c23f01ae
%bcond check 0
%bcond_without bootstrap
%global debug_package %{nil}
%global goipath         github.com/go-openapi/analysis
Version:                1.0.0
%gometa
%global common_description %{expand:
A foundational library to analyze an OAI specification document for easier
reasoning about the content.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Openapi specification object model analyzer
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/analysis-%{version}.tar.gz
%if %{without bootstrap}
%if %{with check}
%endif
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/go-openapi/jsonpointer)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
