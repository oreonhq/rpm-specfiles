%global source0_hash 62a5b972d215cbc3f550d5d251aef1239f271a7f0b57e76f16542775bd6aab20
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/hanwen/go-fuse/v2
Version:                2.11.0
%gometa -f
%global common_description %{expand:
FUSE bindings for Go.}
%global golicenses      LICENSE
%global godocs          example AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        FUSE bindings for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://github.com/hanwen/go-fuse/archive/v%{version}/go-fuse-%{version}.tar.gz
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
