%global source0_hash 67c7331501424de8d178d16d343c577c3707713bd5ccdd06222117a41972df83
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/ebnf
%global forgeurl        https://gitlab.com/cznic/ebnf
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Package ebnf is a library for EBNF grammars.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package ebnf is a library for EBNF grammars
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/ebnf-%{tag}.tar.bz2
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
