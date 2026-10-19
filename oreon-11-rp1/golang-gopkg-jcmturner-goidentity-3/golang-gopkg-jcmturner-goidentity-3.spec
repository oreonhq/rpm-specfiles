%global source0_hash 599b4fc0a2bba638d30c6fbf6748024080221f72d845aedfcfb207dd39ede948
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/jcmturner/goidentity.v3
%global forgeurl        https://github.com/jcmturner/goidentity
Version:                3.0.0
%gometa
%global common_description %{expand:
Standard interface to holding authenticated identities and their attributes.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Standard interface to holding authenticated identities and their attributes
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/goidentity-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/hashicorp/go-uuid)
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
