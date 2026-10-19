%global source0_hash 47f3383068dfc8f134a2adfe8f74fe73170a51db33c3e60409deef70b6364178
%bcond check 1
%global debug_package %{nil}
%global goipath         github.com/vishvananda/netlink
Version:                1.2.1~beta.2
%global tag             v1.2.1-beta.2
%gometa
%global common_description %{expand:
The netlink package provides a simple netlink library for Go. Netlink is the
interface a user-space program in linux uses to communicate with the kernel. It
can be used to add and remove interfaces, set ip addresses and routes, and
configure ipsec. Netlink communication requires elevated privileges, so in most
cases this code needs to be run as root. Since low-level netlink messages are
inscrutable at best, the library attempts to provide an api that is loosely
modeled on the CLI provided by iproute2. Actions like ip link add will be
accomplished via a similarly named function like AddLink(). This library began
its life as a fork of the netlink functionality in docker/libcontainer but was
heavily rewritten to improve testability, performance, and to add new
functionality like ipsec xfrm handling.}
%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple netlink library for go
License:        Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{tag}/netlink-1.2.1-beta.2.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

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
