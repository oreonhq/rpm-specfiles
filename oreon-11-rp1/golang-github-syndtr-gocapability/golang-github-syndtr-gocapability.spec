%global source0_hash 4993ab545cd5832080c4dfcfa9e71b3ed7ebe7e51454c1ac711cf06e5b5ad923
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/syndtr/gocapability
%global commit          42c35b4376354fd554efc7ad35e0b7f94e3a0ffb
%gometa
%global common_description %{expand:
Utilities for manipulating POSIX capabilities in Go.}
%global golicenses      LICENSE
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Utilities for manipulating POSIX capabilities in Go
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/gocapability-%{commit}.tar.gz
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
