%global source0_hash 5d629d0e517ee46ef705d3b507ca824f5bc84306f9b3ae8844370cb1f6647648
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/revel/config
Version:                1.1.0
%gometa
%global common_description %{expand:
This package implements a basic configuration file parser language which
provides a structure similar to what you would find on Microsoft Windows INI
files.}
%global godocs          README.md Doc
Name:           %{goname}
Release:        1%{?dist}
Summary:        Configuration file parser for INI format
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/config-%{version}.tar.gz
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
