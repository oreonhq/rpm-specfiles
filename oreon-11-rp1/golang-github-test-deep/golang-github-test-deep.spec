%global source0_hash ed08d8f98b4620637be97602d4c9e13c0b53e2347bb21a3a0a8f85ad9919b7dd
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-test/deep
Version:                1.1.1
%gometa -L
%global common_description %{expand:
Golang deep variable equality test that returns human-readable differences.}
%global golicenses      LICENSE
%global godocs          CHANGES.md README.md SECURITY.md
Name:           golang-github-test-deep
Release:        1%{?dist}
Summary:        Golang deep variable equality test
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/deep-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
