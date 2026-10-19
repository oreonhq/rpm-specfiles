%global source0_hash e5bba50b0239b74113a218cb11db00fc3dbaf81fdb155cb7e1573cdbd82d9f86
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/charlievieth/fastwalk
Version:                1.0.14
%gometa -L -f
%global common_description %{expand:
Fast parallel directory traversal for Golang.}
%global golicenses      LICENSE go.LICENSE
%global godocs          examples README.md
Name:           golang-github-charlievieth-fastwalk
Release:        1%{?dist}
Summary:        Fast parallel directory traversal for Golang
License:        MIT AND BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/fastwalk-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
%autopatch -q -p1

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
