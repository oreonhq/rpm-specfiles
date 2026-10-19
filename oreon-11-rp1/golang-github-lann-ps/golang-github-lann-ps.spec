%global source0_hash 1d0df31d2532d3f5a5292b6229310ae6ba57b9a0b8756bbbd480767dfb7d8678
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/lann/ps
%global commit          62de8c46ede02a7675c4c79c84883eb164cb71e3
%gometa
%global common_description %{expand:
Persistent data structures for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Persistent data structures for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ps-%{commit}.tar.gz
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
