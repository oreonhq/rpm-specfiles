%global source0_hash ad47429e26a7078df155bffe2d3ff2e967fb0d6be185b5ffe995d6731916bcf7
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/xeipuuv/gojsonschema
Version:                1.2.0
%gometa
%global common_description %{expand:
An implementation of JSON Schema for the Go programming language. Supports
draft-04, draft-06 and draft-07.}
%global golicenses      LICENSE-APACHE-2.0.txt
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Implementation of JSON Schema, draft v4 v6 & v7
License:        ASL 2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gojsonschema-%{version}.tar.gz
Patch0:         0001-Reject-comma-in-time-format.patch
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/xeipuuv/gojsonreference)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

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
