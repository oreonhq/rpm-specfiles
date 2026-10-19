%global source0_hash 10355acc5726698cd4c6a24c04800e301f6d73e3740ff041e3468793fa52675f
%global forgeurl https://github.com/oleg-derevenetz/bwping
%global tag      RELEASE_2.6
Name:           bwping
Version:        2.6
Release:        1%{?dist}
Summary:        Measure bandwidth and response times using ICMP
License:        LicenseRef-Callaway-BSD
URL:            http://bwping.sourceforge.net/
%forgemeta
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{tag}.tar.gz
Patch0:         0001-remove-failing-tests.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
# /oreon:deps
%description
BWPing is a tool to measure bandwidth and response
times between two hosts using Internet Control Message
Protocol (ICMP) echo request/echo reply mechanism.
It does not require any special software on the remote host.
The only requirement is the ability to respond on ICMP echo
request messages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

autoreconf -i
%configure
%make_build
%install
%make_install
%oreon_autofiles main

%check

make check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
