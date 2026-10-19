%global source0_hash f3bef272555f9ffefff504762ec92235cfe50891dedba1c2281d970323d7c367
%ifarch x86_64
%bcond check 1
%else
%bcond check 0
%endif
%bcond bootstrap 0
%global gotestflags -short %{gotestflags}
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/cyphar/filepath-securejoin
Version:                0.7.0
%gometa -L -f
%global common_description %{expand:
An implementation of SecureJoin, a
candidate for inclusion in the Go standard library. The purpose of this function
is to be a "secure" alternative to filepath.Join, and in particular it provides
certain guarantees that are not provided by filepath.Join.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-cyphar-filepath-securejoin
Release:        1%{?dist}
Summary:        Proposed filepath.SecureJoin implementation
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/filepath-securejoin-%{version}.tar.gz
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
