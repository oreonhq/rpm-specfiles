%global source0_hash d3dd19c9e21b534bebc5a44a8699542f6e537dfdd7d67979fb6551a3053ed695
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/schollz/logger
Version:                1.2.0
%gometa
%global common_description %{expand:
Simplistic, opinionated logging for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simplistic, opinionated logging for Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/logger-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

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
