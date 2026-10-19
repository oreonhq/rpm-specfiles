%global source0_hash 27a1d78b876d6a4c4491ae50852f9472de655c5b2fff9bd7a4875519203eef2f
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/sortutil
%global forgeurl        https://gitlab.com/cznic/sortutil
Version:                1.2.1
%global tag             v%{version}
%gometa
%global common_description %{expand:
Utilities supplemental to the Go standard "sort" package.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Utilities supplemental to the Go standard "sort" package
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/sortutil-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
