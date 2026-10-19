%global source0_hash 7cdf89660ee02872aba0331959001b6cc74201388e369224b5299d13a4b95587
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/token
%global forgeurl        https://gitlab.com/cznic/token
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
A variant of the stdlib package token with types FileSet and
Token removed.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A variant of the stdlib package token with types FileSet and Token removed
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/token-%{tag}.tar.bz2
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
