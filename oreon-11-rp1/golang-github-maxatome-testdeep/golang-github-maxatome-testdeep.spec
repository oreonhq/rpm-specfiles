%global source0_hash 072566ea5f4a34d1e9490a99fb430cb17a26061763b7247d1b43d8aafa995960
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/maxatome/go-testdeep
Version:                1.16.0
%gometa -f
%global common_description %{expand:
Extremely flexible golang deep comparison, extends the go testing package,
tests HTTP APIs and provides tests suite.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Tests HTTP APIs and provides tests suite
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-testdeep-%{version}.tar.gz
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
