%global source0_hash 6e7539551865e0c75f785feeb52c480831cd2efd4b5f52989bd35addc283b900
%ifarch x86_64
%bcond check 1
%else
%bcond check 0
%endif
%global debug_package %{nil}
%global goipath         github.com/xtgo/set
Version:                1.0.0
%gometa -L -f
%global common_description %{expand:
General, type-safe, non-allocating set-operations for any sort.Interface.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-xtgo-set
Release:        1%{?dist}
Summary:        General, type-safe, non-allocating set-operations
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/set-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

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
