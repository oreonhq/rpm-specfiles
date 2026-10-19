%global source0_hash f7db4459690a9ada77a27e03f92156395ad2411db0f006f5941c303c9a7cd1a2
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/huandu/xstrings
Version:                1.6.2
%gometa -L -f
%global common_description %{expand:
Go package xstrings is a collection of string functions, which are widely used
in other languages but absent in Go package strings.
All functions are well tested and carefully tuned for performance.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           golang-github-huandu-xstrings
Release:        1%{?dist}
Summary:        Collection of useful string functions in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/xstrings-%{version}.tar.gz
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
