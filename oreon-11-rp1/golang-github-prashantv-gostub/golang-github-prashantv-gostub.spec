%global source0_hash ed08d1297409f9e1c7b07f437727fe0f6e73beef97700bb1d7410995761c1fc9
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/prashantv/gostub
Version:                1.1.0
%gometa -f
%global common_description %{expand:
Gostub is a library to make stubbing in unit tests easy.}
%global golicenses      LICENSE.md
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Gostub is a library to make stubbing in unit tests easy
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gostub-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
