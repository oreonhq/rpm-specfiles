%global source0_hash 3005cf06c9632d4ba516f6f10a195164ef1aa66f1d3e2d90c5fc13338f0d84a6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/jsonreference
Version:                1.0.3
%gometa
%global common_description %{expand:
Fork of gojsonreference with support for structs.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Gojsonreference with support for structs
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jsonreference-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/PuerkitoBio/purell)
BuildRequires:  golang(github.com/go-openapi/jsonpointer)
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
