%global source0_hash 523992ab4bf786eb2e23f7d4e2cb02c9db666feb68400ce3629b17036617927e
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/GeertJohan/go.incremental
Version:                1.0.0
%gometa
%global common_description %{expand:
Go package Incremental provides typed incremental counters that are
concurrency-safe.}
%global golicenses      LICENSE
%global godocs          example README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Concurency-safe incremental numbers
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/go.incremental-%{version}.tar.gz
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
