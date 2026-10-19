%global source0_hash 0bafeab3cb9264bc172ecb3af7dd5d115d69898f422cabd5a52351213e0a8267
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/armon/go-socks5
%global commit          e75332964ef517daa070d7c38a9466a0d687e0a5
%gometa
%global common_description %{expand:
This package provides the socks5 package that implements a SOCKS5 server. SOCKS
(Secure Sockets) is used to route traffic between a client and server through an
intermediate proxy layer. This can be used to bypass firewalls or NATs.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        SOCKS5 server in Golang
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/go-socks5-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/net/context)
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
