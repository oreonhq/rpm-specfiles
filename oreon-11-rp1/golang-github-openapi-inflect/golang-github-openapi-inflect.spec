%global source0_hash 496c9703f128ae8356a7b17c9b93ead79c9e65e2ea5978c8a7b40c0e6f5d928d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/inflect
Version:                1.0.1
%gometa
%global common_description %{expand:
This is a Go library to perform word transformations like pluralization,
singularization, etc. It is a fork of https://bitbucket.org/pkg/inflect.}
%global golicenses      LICENCE
%global godocs          README
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go library to perform word transformations
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/inflect-%{version}.tar.gz
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
