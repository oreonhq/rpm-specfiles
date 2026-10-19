%global source0_hash 7d82b9bb7291adbe7498fe946920ab3e7fc9e6cbfc3b2294693fad00bf0dd17e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/davecgh/go-spew
Version:                1.1.1
%gometa
%global common_description %{expand:
Go-spew implements a deep pretty printer for Go data structures to aid in
debugging. A comprehensive suite of tests with 100% test coverage is
provided to ensure proper functionality.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implements a deep pretty printer for Go data structures to aid in debugging
License:        ISC
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-spew-%{version}.tar.gz
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
