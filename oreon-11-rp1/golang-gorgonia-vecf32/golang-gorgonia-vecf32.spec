%global source0_hash ea6a1b81d308e96327f6b13b7817eb263d64f3b40e48472108881588bbac1e49
%bcond check 1
%bcond bootstrap 0
%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif
%global goipath         gorgonia.org/vecf32
%global forgeurl        https://github.com/gorgonia/vecf32
Version:                0.9.0
%gometa -L -f
%global common_description %{expand:
Package vecf32 provides common functions and methods for slices of float32.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTORS.md README.md
Name:           golang-gorgonia-vecf32
Release:        1%{?dist}
Summary:        Package vecf32 provides common functions and methods for slices of float32
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/vecf32-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A

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
