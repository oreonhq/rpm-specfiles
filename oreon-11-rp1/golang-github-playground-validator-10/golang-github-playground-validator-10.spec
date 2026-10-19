%global source0_hash 91ef7d50e3cf2da25c1ce502621d2a8476a0df0eacd5478d486529f71e6a8d01
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-playground/validator/v10
%global forgeurl        https://github.com/go-playground/validator
Version:                10.30.5
%gometa
%global goaltipaths     gopkg.in/go-playground/validator.v10
%global common_description %{expand:
Package Validator implements value validations for structs and individual fields
based on tags.
It can also handle Cross-Field and Cross-Struct validation for nested structs
and has the ability to dive into arrays and maps of any type.}
%global golicenses      LICENSE
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go struct and field validation
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/validator-%{version}.tar.gz
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
