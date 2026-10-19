%global source0_hash e75b7bef8da7ac8e26a8dd488f7b473766f3db6ed16693737fdc99522a26156a
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/hashicorp/go-version
Version:                1.9.0
%gometa -L -f
%global common_description %{expand:
Go-version is a library for parsing versions and version constraints, and
verifying versions against a set of constraints. go-version can sort a
collection of versions properly, handles prerelease/beta versions, can increment
versions, etc.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           golang-github-hashicorp-version
Release:        1%{?dist}
Summary:        Go library for parsing and verifying versions and version constraints
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-version-%{version}.tar.gz
Patch:          %{gourl}/pull/151.patch
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
