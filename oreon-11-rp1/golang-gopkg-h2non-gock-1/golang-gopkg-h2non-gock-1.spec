%global source0_hash b516b35c9a21cfc31f582806db95c8d14565e54f98aba7b56319a16d5f8d3128
%bcond check 1
%global debug_package %{nil}
%global goipath         gopkg.in/h2non/gock.v1
%global forgeurl        https://github.com/h2non/gock
Version:                1.0.16
%gometa
%global goaltipaths     github.com/h2non/gock
%global common_description %{expand:
Versatile HTTP mocking made easy in Go for net/http stdlib package.}
%global golicenses      LICENSE
%global godocs          _examples History.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Expressive HTTP traffic mocking and testing made easy in Go
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gock-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/h2non/parth)
BuildRequires:  golang(github.com/nbio/st)
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
