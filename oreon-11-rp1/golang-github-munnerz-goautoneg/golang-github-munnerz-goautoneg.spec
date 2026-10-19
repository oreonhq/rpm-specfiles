%global source0_hash bf4a8e226cee11772f6911ae948f29022360f53d857b9b22104b3c5166bc132f
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         github.com/munnerz/goautoneg
%global commit          a7dc8b61c822528f973a5e4e7b272055c6fdb43e
%gometa -L -f
%global common_description %{expand:
HTTP Content-Type Autonegotiation.}
%global golicenses      LICENSE
%global godocs          README.txt
Name:           golang-github-munnerz-goautoneg
Version:        0
Release:        1%{?dist}
Summary:        HTTP Content-Type Autonegotiation
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/goautoneg-%{commit}.tar.gz
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
