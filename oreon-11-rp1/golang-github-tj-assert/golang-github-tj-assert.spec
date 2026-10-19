%global source0_hash 1596d9e6f2ba75f1b5e4b9b8f4a86ac4834723f1abaff4a717ba8c6896387f05
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/tj/assert
Version:                0.0.3
%gometa -L -f
%global common_description %{expand:
Testify/assert but as testify/require.}
%global golicenses      LICENSE
%global godocs          Readme.md
Name:           golang-github-tj-assert
Release:        1%{?dist}
Summary:        Testify/assert but as testify/require
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/assert-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
