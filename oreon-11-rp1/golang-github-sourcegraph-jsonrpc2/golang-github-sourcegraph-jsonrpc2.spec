%global source0_hash 07d53e5579d8e3310ffeb39bb606141561b8e6561965d6431eaf93d92831a091
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/sourcegraph/jsonrpc2
Version:                0.1.0
%gometa
%global common_description %{expand:
Package jsonrpc2 provides a client and server implementation of JSON-RPC 2.0.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Package jsonrpc2 provides a client and server implementation of JSON-RPC 2.0
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/jsonrpc2-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/gorilla/websocket)
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
