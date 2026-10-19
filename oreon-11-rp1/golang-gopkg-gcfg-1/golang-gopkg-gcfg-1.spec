%global source0_hash 3d60ba7a07e7d7d831a756f565c7fdc75895f294b2b69185674bb0ed70622645
%bcond check 0
%global debug_package %{nil}
%global goipath         gopkg.in/gcfg.v1
%global forgeurl        https://github.com/go-gcfg/gcfg
Version:                1.2.3
%gometa
%global godevelheader %{expand:
Obsoletes:      golang-googlecode-gcfg-devel < 0-0.17
Obsoletes:      golang-gopkg-gcfg-devel < 0-0.17
Obsoletes:      golang-googlecode-gcfg-unit-test < 0-0.17
}
%global common_description %{expand:
Read ini-style configuration files into go structs; supports user-defined types
and subsections.}
%global golicenses      LICENSE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Read ini-style configuration files into go structs
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/gcfg-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(gopkg.in/warnings.v0)
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

%gocheck -d types
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
