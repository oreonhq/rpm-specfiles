%global source0_hash dcc74b4158f0139506ad58e5ce9695c05b115aaa9011a2edacb492fc3d99def6
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/modern-go/concurrent
Version:                1.0.3
%global tag             1.0.3
%gometa
%global common_description %{expand:
Concurrency utilities for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Concurrency utilities for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{version}/concurrent-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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
