%global source0_hash fe088ec5d296bfc7f152eb16d5a069526973f6f1f079fdde5ba70e3c3443d25e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golang-sql/civil
%global commit          cb61b32ac6fe84d34b81730175f91965e43d0f90
%gometa
%global common_description %{expand:
Civil Date and Time package for Go.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Civil Date and Time package for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/civil-%{commit}.tar.gz
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
