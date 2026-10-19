%global source0_hash 676b99c051fef68d1b0fb0385103de0e42a3ee556919b2b54ff5d3445bac56dd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/vmihailenco/tagparser/v2
Version:                2.0.0
%gometa
%global common_description %{expand:
Opinionated Golang tag parser.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Opinionated Golang tag parser
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://github.com/vmihailenco/tagparser/archive/v%{version}/tagparser-%{version}.tar.gz
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
