%global source0_hash cb32b383422a9aae11d260657d52a3789bd799802881b9ced3ee82c370be6f76
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/opentracing/opentracing-go
Version:                1.2.0
%gometa
%global common_description %{expand:
This package is a Go platform API for OpenTracing.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        OpenTracing API for Go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/opentracing-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/stretchr/testify/suite)
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
