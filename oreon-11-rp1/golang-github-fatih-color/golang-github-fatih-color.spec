%global source0_hash 1ea4633f59411fe3d25d10950f223021c913f4ff4b95286ab94e0bc641c1b246
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/fatih/color
Version:                1.19.0
%gometa -L -f
%global common_description %{expand:
Color lets you use colorized outputs in terms of ANSI Escape Codes in Go. It has
support for Windows too! The API can be used in several ways, pick one that
suits you.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           golang-github-fatih-color
Release:        1%{?dist}
Summary:        Color package for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/color-%{version}.tar.gz
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
