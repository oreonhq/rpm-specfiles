%global source0_hash 6a52923fb97e51860c9de7e7b65894eb65de03d0da496a6bbd04bca01cab537d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/marcinbor85/gohex
%global commit          baab2527a9a2a4abb3dc06baabedfa5e0268b8d8
%gometa
%global common_description %{expand:
A Go library for parsing Intel HEX files.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go library for parsing Intel HEX files
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gohex-%{commit}.tar.gz
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
