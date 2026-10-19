%global source0_hash 1dd93521aae1bc732ed4baa8d33998665142a2ca6cdbf16cbe136a6a147d35d0
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jawher/mow.cli
Version:                1.2.0
%gometa
%global common_description %{expand:
Package Cli provides a framework to build command line applications in Go with
most of the burden of arguments parsing and validation placed on the framework
instead of the user.}
%global golicenses      LICENSE
%global godocs          README.md README.md.template
Name:           %{goname}
Release:        1%{?dist}
Summary:        Versatile library for building CLI applications in Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/mow.cli-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
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
