%global source0_hash 3dd467f7a892d86c72f8320581498aa0564dd0657d944cc96ca7f301efbf5878
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/asaskevich/govalidator
Version:                12.0.0
%gometa
%global common_description %{expand:
Package Govalidator is package of validators and sanitizers for strings, structs
and collections.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Validators and sanitizers for strings, numerics, slices and structs
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/govalidator-%{version}.tar.gz
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
