%global source0_hash 8760b84a1b5cd49ce81a56c9fce0ba0de157355b1bb38d112bdfd7cf7ad7a44d
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/gorilla/handlers
Version:                1.5.2
%gometa
%global common_description %{expand:
Package handlers is a collection of handlers (aka "HTTP middleware") for use
with Go's net/http package (or any framework supporting http.Handler).
The package includes handlers for logging in standardised formats, compressing
HTTP responses, validating content types and other useful tools for manipulating
requests and responses.}
%global golicenses      LICENSE
%global godocs          README.md
%global gosupfiles      glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Collection of useful handlers for go's net/http package
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/handlers-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/felixge/httpsnoop)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

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
