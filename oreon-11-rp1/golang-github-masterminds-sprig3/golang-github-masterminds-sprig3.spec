%global source0_hash bf74b78c51c2e5e0b181a3edc5d5787dcf70757d30f8a002df77be594fa8b8d1
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/Masterminds/sprig/v3
Version:                3.3.0
%gometa -L -f
%global common_description %{expand:
Useful template functions for Go templates.}
%global golicenses      LICENSE.txt
%global godocs          docs CHANGELOG.md README.md
Name:           golang-github-masterminds-sprig3
Release:        1%{?dist}
Summary:        Useful template functions for Go templates
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/Masterminds/sprig/archive/v%{version}/sprig-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

# Remove test requiring connection
rm -rf network_test.go

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
