%global source0_hash bcad16d5bbe4e778a4df9a2150afa45663682bdbab8bf970fec420ced579ffa6
%bcond check 1
%global debug_package %{nil}
%global goipath         nhooyr.io/websocket
%global forgeurl        https://github.com/nhooyr/websocket
Version:                1.8.12
%gometa
%global common_description %{expand:
Minimal and idiomatic WebSocket library for Go.}
%global golicenses      LICENSE.txt
%global godocs          examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Minimal and idiomatic WebSocket library for Go
License:        MIT
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/websocket-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gin-gonic/gin)
BuildRequires:  golang(github.com/gobwas/ws)
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(github.com/google/go-cmp/cmp)
BuildRequires:  golang(github.com/google/go-cmp/cmp/cmpopts)
BuildRequires:  golang(github.com/gorilla/websocket)
BuildRequires:  golang(github.com/klauspost/compress/flate)
BuildRequires:  golang(golang.org/x/time/rate)
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
