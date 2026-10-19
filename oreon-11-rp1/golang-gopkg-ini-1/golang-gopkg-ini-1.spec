%global source0_hash 06ba51234140118d1b6064f1817aa89cc971c6e7ce04cb9d286e6660d89296c8
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/ini.v1
%global forgeurl        https://github.com/go-ini/ini
Version:                1.67.0
%gometa
%global goaltipaths     github.com/go-ini/ini
%global common_description %{expand:
Package ini provides INI file read and write functionality in Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package ini provides INI file read and write functionality in Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/ini-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
