%global source0_hash 9133ffda0d6923d309809baf432c368327f355963d2182e57040b6318c41fcf2
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/chzyer/readline
Version:                1.5.1
%gometa -L -f
%global common_description %{expand:
Readline is a pure Go implementation for GNU-Readline like library.}
%global golicenses      LICENSE
%global godocs          example CHANGELOG.md README.md
Name:           golang-github-chzyer-readline
Release:        1%{?dist}
Summary:        Pure Go implementation of GNU Readline-like library
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/readline-%{version}.tar.gz
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
