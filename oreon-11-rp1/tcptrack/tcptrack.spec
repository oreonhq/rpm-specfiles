%global source0_hash 8725205ecbeddc3f891e3345e70f150d87705b099eafd8780f4739ab14f8c862

Name:           tcptrack
Version:        1.4.3
Release:        17%{?dist}
Summary:        Displays information about tcp connections on a network interface

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/bchretien/tcptrack
Source0:        https://github.com/bchretien/tcptrack/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Build on F36+ has stronger argument type checking and needs this patch
# was already reported upstream in https://github.com/bchretien/tcptrack/pull/10/
# line changed
Patch0:         https://github.com/bchretien/tcptrack/commit/409007afbce8ec5a81312a2a4123dd83b62b4494.patch#/tcptrack-1.4.3-type-mismatch.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires:  libpcap-devel

%description
tcptrack is a sniffer which displays information about TCP connections
it sees on a network interface. It passively watches for connections on 
the network interface, keeps track of their state and displays a list of
connections in a manner similar to the unix 'top' command. It displays 
source and destination addresses and ports, connection state, idle time, 
and bandwidth usage

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.*

%changelog
%autochangelog
