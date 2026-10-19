%global source0_hash 15615ff760c55a7024d362fccbbf75646e20235472ab24c8ef94792876f196eb
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/jackc/puddle/v2
Version:                2.2.2
%gometa -L -f
%global common_description %{expand:
Generic resource pool for Go.}
%global golicenses      LICENSE
%global godocs          README.md CHANGELOG.md
Name:           golang-github-jackc-puddle2
Release:        1%{?dist}
Summary:        Generic resource pool for Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/jackc/puddle/archive/v%{version}/puddle-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep -A
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
