%global source0_hash 3aec3f3f8bac49d8b411e41168a1493420e267cb1367114270e9070c2a915f6d
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/hugelgupf/socketpair
%global commit          05d35a94e71444d53460c2b34dfb3dc87c99d0bd
%gometa
%global common_description %{expand:
socketpair is a Go library that provides bidirectionally connected net.Conns,
net.PacketConns made from socketpair(2) as well as bidirectionally connected
net.TCPConns.
socketpair is currently mostly used in testing Go protocol libraries.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Go library that provides bidirectionally connected Conns
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/socketpair-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
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
