%global source0_hash 8e2d51f9d68aa733fdad8fbc0f90eb951e26b96437b09f17c1a7bcfd114517a5
%global commit 7cb788c9c43facfd2d14ff50e16d6a19f033a6a7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170912
%global git_ver -git%{gitdate}.%{shortcommit}
%global git_rel .git%{gitdate}.%{shortcommit}
Name:		bluez-tools
Version:	0.2.0
Release:        1%{?dist}
Summary:        A set of tools to manage Bluetooth devices for Linux
License:	GPL-2.0-or-later
URL:		https://github.com/khvzak/%{name}
Source0:        https://github.com/khvzak/%{name}/archive/%{commit}/%{name}-%{version}-git%{gitdate}.%{shortcommit}.tar.gz
Patch0:		%{url}/pull/34.patch#/fix_gcc-10_compile.patch
Patch1:		%{name}-exit-if-no-adapter.patch
Requires:	bluez%{?_isa}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  readline-devel
# /oreon:deps
%description
This was a GSoC'10 project to implement a new command line tools for
bluez (Bluetooth stack for Linux).  It is currently an active open
source project.

The project is implemented in C and uses the D-Bus interface of bluez.

The project is still a work in progress, and not all APIs from Bluez
have been implemented as a part of bluez-tools.  The APIs which have
been implemented in bluez-tools are adapter, agent, device, network
and obex.  Other APIs, such as interfaces for medical devices,
pedometers and other specific APIs have not been ported to bluez-tools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p 1
%{_bindir}/autoreconf -fiv

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
