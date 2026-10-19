%global source0_hash a01c6644fc2e1403a4489306a4fbca52dd3b2e1b6374e6a2f86f57fd430104be
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/matryer/try
Version:                1
%gometa
%global common_description %{expand:
Simple idiomatic retry package for Go.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple idiomatic retry package for Go
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/try-%{version}.tar.gz
Patch0001:      https://github.com/matryer/try/pull/7.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/cheekybits/is)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

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
