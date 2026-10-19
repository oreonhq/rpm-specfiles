%global source0_hash 2d925e457aba4c3c4c3198e87578ec212f1be1711b9151a7e86ad19aadbe9c0a
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         gorgonia.org/vecf64
%global forgeurl        https://github.com/gorgonia/vecf64
Version:                0.9.0
%gometa -L -f
%global common_description %{expand:
Package vec64 provides common functions and methods for slices of float64.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTORS.md README.md
Name:           golang-gorgonia-vecf64
Release:        1%{?dist}
Summary:        Package vecf64 provides common functions and methods for slices of float64
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/vecf64-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

# Unused
rm asm_vecExp_avx.s

%if %{without bootstrap}
%install
%gopkginstall
%oreon_autofiles main
%if %{without bootstrap}
%if %{with check}
%check

%gocheck
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
