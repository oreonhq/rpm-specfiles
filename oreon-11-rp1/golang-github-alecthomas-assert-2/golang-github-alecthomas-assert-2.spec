%global source0_hash 56f776f1d5e1888ef35b4c01ae96dd7d47f706911288a774b5bc199dcec734da
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/alecthomas/assert/v2
Version:                2.11.0
%gometa -f
%global common_description %{expand:
A simple assertion library using Go generics.}
%global golicenses      COPYING
%global godocs          README.md bin/README.hermit.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A simple assertion library using Go generics
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/alecthomas/assert/archive/v%{version}/assert-%{version}.tar.gz
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
