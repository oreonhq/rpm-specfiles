%global source0_hash 5e535665017ab0cbd72c6216621f959f14151ef57694af5fde93edabea4ff1c5
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/parser
%global forgeurl        https://gitlab.com/cznic/parser
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Collection of Go parsers.}
%global golicenses      LICENSE
%global godocs          README.md AUTHORS-nquads CONTRIBUTORS-nquads\\\
                        AUTHORS-yacc CONTRIBUTORS-yacc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Collection of Go parsers
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/parser-%{tag}.tar.bz2
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
# nquads and yacc share same license.
cp nquads/LICENSE .
cp nquads/AUTHORS nquads-AUTHORS
cp nquads/CONTRIBUTORS nquads-CONTRIBUTORS
cp yacc/AUTHORS yacc-AUTHORS
cp yacc/CONTRIBUTORS yacc-CONTRIBUTORS

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
