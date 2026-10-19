%global source0_hash c8841ece8f1983e64ec68a6a85f63faf117138263598d25f2a4a0fd00ee013d2
%global debug_package %{nil}
%bcond check 0
%global goipath         github.com/d2g/dhcp4server
%global commit          7d4a0a7f59a572d629ba5f49634b35c7fac7967e
%gometa
%global common_description %{expand:
DHCP Server for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        DHCP Server for Go
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/dhcp4server-%{commit}.tar.gz
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
