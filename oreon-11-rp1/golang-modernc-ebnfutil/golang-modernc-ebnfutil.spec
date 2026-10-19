%global source0_hash 634712122a5e73170c7ed861cc243f64222c5a767e08e4332a98e48adb380e29
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/ebnfutil
%global forgeurl        https://gitlab.com/cznic/ebnfutil
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Package ebnfutils provides some utilities for messing with EBNF grammars.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package ebnfutils provides some utilities for messing with EBNF grammars
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ebnfutil-%{tag}.tar.bz2
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
