%global source0_hash de65fbbf4d0b89fd356a79a10e1a55904739d6a549484e8bdb118d5efb71d11c
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/mikioh/ipaddr
%global commit          d465c8ab672111787b24b8f03326449059a4aa33
%gometa
%global common_description %{expand:
Package ipaddr provides basic functions for the manipulation of IP address
prefixes and subsequent addresses as described in RFC 4632 and RFC 4291.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Basic functions for the manipulation of IP address prefixes
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/ipaddr-%{commit}.tar.gz
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
