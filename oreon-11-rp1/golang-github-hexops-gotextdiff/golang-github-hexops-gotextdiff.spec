%global source0_hash 95ca5abd3c132e04ca1a0deeeac130b6bfe871e504e3775cb53e43ad3fc8183d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hexops/gotextdiff
Version:                1.0.3
%gometa -f
%global common_description %{expand:
Unified text diffing in Go (copy of the internal diffing packages the official
Go language server uses).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Unified text diffing in Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gotextdiff-%{version}.tar.gz
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
