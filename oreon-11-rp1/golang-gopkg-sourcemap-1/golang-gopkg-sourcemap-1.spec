%global source0_hash a02ff67183c8c01f2f1c1cb4e716200fcc56f61766922cd18576c8f203007aae
%bcond check 1
%global debug_package %{nil}
%global goipath         gopkg.in/sourcemap.v1
%global forgeurl        https://github.com/go-sourcemap/sourcemap
Version:                1.0.5
%gometa
%global common_description %{expand:
Source maps consumer for Golang.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Source maps consumer for Golang
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/sourcemap-%{version}.tar.gz
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
