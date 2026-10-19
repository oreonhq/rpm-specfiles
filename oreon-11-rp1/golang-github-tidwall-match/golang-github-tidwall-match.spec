%global source0_hash 1fc2ff17ecdd82c7ba739b4f373b9df731a8e42517c70285c8bbf24dd9b3f2f0
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/tidwall/match
Version:                1.1.1
%gometa -L -f
%global common_description %{expand:
Simple string pattern matcher for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-tidwall-match
Release:        1%{?dist}
Summary:        Simple string pattern matcher for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/match-%{version}.tar.gz
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
