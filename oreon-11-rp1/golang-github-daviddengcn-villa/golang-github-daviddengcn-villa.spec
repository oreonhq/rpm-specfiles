%global source0_hash 03180091ae36638b72cbde6c45fc40ca62c2c37175f3a8207e8051c029f8a750
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/daviddengcn/go-villa
%global commit          68107afb6d76df5bc1ab7fdaae3c79793f656be9
%gometa
%global common_description %{expand:
Some helper types for go: priority queue, slice wrapper.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Priority queue and slice wrappers for Go
License:        BSD-2-Clause-Views
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-villa-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golangplus/bytes)
BuildRequires:  golang(github.com/golangplus/sort)
BuildRequires:  golang(github.com/golangplus/testing/assert)
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
