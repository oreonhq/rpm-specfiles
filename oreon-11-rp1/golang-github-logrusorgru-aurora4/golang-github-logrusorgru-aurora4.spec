%global source0_hash 3f7402d669558413c34530d7afcbf10aa2485df9f6241742134c5e04a20f6828
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/logrusorgru/aurora/v4
Version:                4.0.0
%gometa -L -f
%global common_description %{expand:
Golang ultimate ANSI-colors that supports Printf/Sprintf methods.}
%global golicenses      LICENSE
%global godocs          AUTHORS.md CHANGELOG.md README.md
Name:           golang-github-logrusorgru-aurora4
Release:        1%{?dist}
Summary:        Golang ultimate ANSI-colors that supports Printf/Sprintf methods
License:        Unlicense
URL:            %{gourl}
Source0:        https://github.com/logrusorgru/aurora/archive/v%{version}/aurora-%{version}.tar.gz
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
