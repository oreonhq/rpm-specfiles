%global source0_hash 94edd9e105ee82ff865c75a71ae88f569d208208c78c0264e1b664f2d02d0b83
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/golangplus/sort
Version:                1.0.0
%gometa
%global common_description %{expand:
Plus to standard sort package.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Plus to standard sort package
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/sort-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
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
