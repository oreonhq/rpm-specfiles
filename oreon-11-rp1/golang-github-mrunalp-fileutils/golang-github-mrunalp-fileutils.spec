%global source0_hash a463fa845d24eb587929b9777512bcf0f3ff11d4d9a4b133b27f397fb48e6a75
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/mrunalp/fileutils
Version:                0.5.1
%gometa -L
%global common_description %{expand:
Collection of utilities for file manipulation in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           golang-github-mrunalp-fileutils
Release:        1%{?dist}
Summary:        Collection of utilities for file manipulation in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fileutils-%{version}.tar.gz
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
