%global source0_hash 707f217e9a46c516c289b71c45a4e51b11b5e0fcec54c1fbfecde47b8a001799
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/gorilla/websocket
Version:                1.5.3
%gometa
%global common_description %{expand:
A fast, well-tested and widely used WebSocket implementation for Go.}
%global golicenses      LICENSE
%global godocs          examples AUTHORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A fast, well-tested and widely used WebSocket implementation for Go
License:        BSD-2-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/websocket-%{version}.tar.gz
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
