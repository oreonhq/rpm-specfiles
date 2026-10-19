%global source0_hash a6ad99106d7c93fee50a9b8c68c34afca5b0fe5dcd63a62f3017a90f36ac9af5
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/retry.v1
%global forgeurl        https://github.com/go-retry/retry
Version:                1.0.3
%gometa
%global common_description %{expand:
Package retry provides a framework for retrying actions. It does not itself
invoke the action to be retried, but is intended to be used in a retry loop.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple retry mechanism for Go
License:        LGPL-3.0-or-later WITH LGPL-3.0-linking-exception
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/retry-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1
sed -i "s|github.com/rogpeppe/clock|github.com/juju/clock|" $(find . -iname "*.go" -type f)
# Needs github.com/juju/clock which needs too many deps with no other use
rm -rfv retry_test.go

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
