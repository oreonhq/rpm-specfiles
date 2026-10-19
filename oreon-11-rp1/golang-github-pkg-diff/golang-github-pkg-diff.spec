%global source0_hash 45829e1dda9d3b888150f7f8b7a263a33278d1e2568ba9a6e1da14649f183478
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/pkg/diff
%global commit          20ebb0f2a09e612109b224b32f79370409108bcc
%gometa
%global common_description %{expand:
Module github.com/pkg/diff can be used to create, modify, and print diffs.
The top level package, diff, contains convenience functions for the most common
uses.
The subpackages provide very fine-grained control over every aspect:
- myers: creates diffs using the Myers diff algorithm.
- edit: contains the core diff data types.
- ctxt: provides tools to reduce the amount of context in a diff.
- write: provides routines to write diffs in standard formats.}
%global golicenses      LICENSE
%global godocs          readme.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Create, modify, and print diffs
License:        BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/diff-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
