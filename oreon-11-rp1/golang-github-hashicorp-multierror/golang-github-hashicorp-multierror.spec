%global source0_hash 8d1bb3377310e8ffe4c7b5672c5de1eaed153402aebd15d6e5b9673c356a065f
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hashicorp/go-multierror
Version:                1.1.1
%gometa
%global common_description %{expand:
Go-multierror is a package for Go that provides a mechanism for representing a
list of error values as a single error.
This allows a function in Go to return an error that might actually be a list of
errors. If the caller knows this, they can unwrap the list and access the
errors. If the caller does not know, the error formats to a nice human-readable
format.
Go-multierror implements the errwrap interface so that it can be used with that
library, as well.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go package for representing a list of errors as a single error
License:        MPL-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go-multierror-%{version}.tar.gz
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
