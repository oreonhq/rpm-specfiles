%global source0_hash 3433c82078d09d5e25fbb6767b5328b16f7f0462580b39e0cba4d488d21c5f09
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/rogpeppe/fastuuid
Version:                1.2.0
%gometa
%global common_description %{expand:
Package fastuuid provides fast UUID generation of 192 bit universally unique
identifiers. It does not provide formatting or parsing of the identifiers
(it is assumed that a simple hexadecimal or base64 representation is
sufficient, for which adequate functionality exists elsewhere).}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Fast generation of 192-bit UUIDs
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fastuuid-%{version}.tar.gz
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
