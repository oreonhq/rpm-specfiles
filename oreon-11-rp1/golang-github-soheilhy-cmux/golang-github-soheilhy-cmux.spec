%global source0_hash 199232ece74332f408a38e4d38e7ca942b3e66ae58074ca95d3f069693e0dca1
%bcond check 0
%global debug_package %{nil}
%global goipath         github.com/soheilhy/cmux
Version:                0.1.5
%gometa
%global common_description %{expand:
Cmux is a generic Go library to multiplex connections based on their payload.
Using cmux, you can serve gRPC, SSH, HTTPS, HTTP, Go RPC, and pretty much any
other protocol on the same TCP listener.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTORS README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Connection multiplexer for Go: serve different services on the same port
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/cmux-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/net/http2)
BuildRequires:  golang(golang.org/x/net/http2/hpack)
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
