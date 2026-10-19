%global source0_hash 9781a79a5b46e6ad245d238d1be1b37d8eab9ca9e57edb575ef0af158adeeefb
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/jcmturner/dnsutils.v1
%global forgeurl        https://github.com/jcmturner/dnsutils
Version:                1.0.1
%gometa
%global common_description %{expand:
DNS utilities for Go.}
%global golicenses      LICENSE
Name:           %{goname}
Release:        1%{?dist}
Summary:        DNS utilities for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/dnsutils-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
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
