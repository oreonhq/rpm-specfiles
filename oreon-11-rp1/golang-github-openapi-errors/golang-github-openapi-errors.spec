%global source0_hash bb7354b64cc760ca057ba88d2651210b855c138b105cdbe86e57c494f3d53a9f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/go-openapi/errors
Version:                0.22.9
%gometa -L
%global common_description %{expand:
Package Errors provides an Error interface and several concrete types
implementing this interface to manage API errors and JSON-schema validation
errors.
A middleware handler ServeError() is provided to serve the errors types it
defines.
It is used throughout the various Go-openapi toolkit libraries.}
%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md
Name:           golang-github-openapi-errors
Release:        1%{?dist}
Summary:        Openapi toolkit common errors
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/errors-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -p1

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
