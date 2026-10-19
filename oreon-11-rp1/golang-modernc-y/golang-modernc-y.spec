%global source0_hash 153efcaace83992925bb4daafb3190c007a38c5b810fc4bcc8e7eebfc9bcf78f
%bcond check 0
%global debug_package %{nil}
%global goipath         modernc.org/y
%global forgeurl        https://gitlab.com/cznic/y
Version:                1.1.0
%global tag             v%{version}
%gometa -f
%global common_description %{expand:
Converts .y (yacc) source files to data suitable for a parser
generator.}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Converts .y (yacc) source files to data suitable for a parser generator
License:        BSD-3-Clause and GPL-2.0-only and MIT
URL:            %{gourl}
Source0:        %{forgeurl}/-/archive/%{tag}/y-%{tag}.tar.bz2
Patch0001:      0001-Fix-build-with-Go-1.24.patch
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
