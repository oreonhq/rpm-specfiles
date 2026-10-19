%global source0_hash 4f47d88cbab61e0279ca3adb18eba00dd0624d4eddecdc232c53e8f84ba4ca64
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/lexer
%global forgeurl        https://gitlab.com/cznic/lexer
Version:                1.0.2
%global tag             v1.0.2
%gometa
%global common_description %{expand:
Run time generator of action less scanners (lexeme recognizers).}
%global golicenses      LICENSE LICENSE-GO
%global godocs          AUTHORS CONTRIBUTORS README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Run time generator of action less scanners
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/lexer-%{tag}.tar.bz2
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
