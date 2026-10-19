%global source0_hash 4ec57839cacb49d87fe22d4ee4286daf4944808d9af09739d218c62255f364b7
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/jcmturner/rpc.v1
%global forgeurl        https://github.com/jcmturner/rpc
Version:                1.1.0
%gometa
%global common_description %{expand:
Remote Procedure Call libraries
(http://pubs.opengroup.org/onlinepubs/9629399/).}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Remote Procedure Call libraries
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/rpc-%{version}.tar.gz
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
