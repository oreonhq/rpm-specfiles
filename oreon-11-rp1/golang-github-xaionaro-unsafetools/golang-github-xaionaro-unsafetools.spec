%global source0_hash ceab88cd12c9379daab12ffd303eb58788171d2b58353e6d8e6e05aab7fa8780
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xaionaro-go/unsafetools
%global commit          4686db630395367dffebe4dc767686d62cc55e73
%gometa
%global common_description %{expand:
This package provides a FieldByName function to access to any field (including
private/unexported) of a structure. This is meant to be used for unit-tests
only.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Access to private/unexported fields of a structure
License:        CC0-1.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/unsafetools-%{commit}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
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
