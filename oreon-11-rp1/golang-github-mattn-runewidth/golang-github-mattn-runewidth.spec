%global source0_hash 2e759a73761eab936c67093e8d7d5b7375eb3839dbd96133748ba006715b438e
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/mattn/go-runewidth
Version:                0.0.30
%gometa -L
%global common_description %{expand:
Package go-runewidth provides functions to get fixed width of a character or
string.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-mattn-runewidth
Release:        1%{?dist}
Summary:        Functions for getting fixed width of a character or string
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-runewidth-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
