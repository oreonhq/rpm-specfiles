%global source0_hash 0c291289872c0ecc913b06f08cff3d29949e1db7fe5786ebb16d7737d88d2af1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-macaron/inject
%global commit          138e5925c53bc4b58f90b4787ad7a682c4c6498f
%gometa
%global common_description %{expand:
Package inject provides utilities for mapping and injecting dependencies in
various ways.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Utilities for mapping and injecting dependencies in various ways
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/inject-%{commit}.tar.gz
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
