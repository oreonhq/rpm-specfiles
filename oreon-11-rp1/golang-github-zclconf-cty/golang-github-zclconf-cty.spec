%global source0_hash e7c109b42bddc885061e73bd2cf04bc64e1e2a2c49c2e18e6f140c9974d39d25
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/zclconf/go-cty
Version:                1.16.0
%gometa -L
%global common_description %{expand:
A type system for dynamic values in Go applications.}
%global golicenses      LICENSE
%global godocs          docs CHANGELOG.md COMPATIBILITY.md README.md
Name:           golang-github-zclconf-cty
Release:        1%{?dist}
Summary:        A type system for dynamic values in Go applications
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-cty-%{version}.tar.gz
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

%ifarch %{ix86}
%gocheck -d cty/function/stdlib
%else
%gocheck
%endif
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
