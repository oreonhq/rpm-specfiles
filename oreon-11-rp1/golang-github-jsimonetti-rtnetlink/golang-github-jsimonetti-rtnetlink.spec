%global source0_hash fab1f59db068c705f1dc8dbb9120180dd7710a1c950c23ff0cf6ee6052d2c582
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jsimonetti/rtnetlink
Version:                2.2.0
%gometa -L -f
%global common_description %{expand:
Package rtnetlink provides low-level access to the Linux rtnetlink API. MIT
Licensed.}
%global golicenses      LICENSE.md
%global godocs          README.md
Name:           golang-github-jsimonetti-rtnetlink
Release:        1%{?dist}
Summary:        Package rtnetlink provides low-level access to the Linux rtnetlink API. MIT Licensed
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/rtnetlink-%{version}.tar.gz
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
