%global source0_hash 97f7598bd77f1fbb21f86350907ce359b3964c150dc6ffc237eb87c606bedad2
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/juju/gnuflag
Version:                1.0.0
%gometa -f
%global common_description %{expand:
GNU-compatible flag handling with a stdlib-like API for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        GNU-compatible flag handling with a stdlib-like API for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gnuflag-%{version}.tar.gz
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
