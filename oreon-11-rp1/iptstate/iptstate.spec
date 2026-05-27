%global source0_hash 896df0602885456a2631f795d634fc21311e505f8c910348e6312860f2097955

Name: iptstate
Summary: A top-like display of IP Tables state table entries
Version: 2.2.7
Release: 11%{?dist}
Source: https://github.com/jaymzh/iptstate/releases/download/v%{version}/iptstate-%{version}.tar.bz2
Patch01: 0001-Makefile-respect-LDFLAGS.patch
Patch02: 0002-Makefile-Use-pkg-config.patch
Patch03: 0003-Makefile-don-t-override-CPPFLAGS.patch
Patch04: 0004-Cleanup-table-entry-17-18.patch
URL: http://www.phildev.net/iptstate/
License: zlib
Requires: iptables
BuildRequires:  gcc-c++
BuildRequires: ncurses-devel
BuildRequires: libnetfilter_conntrack-devel
BuildRequires: make

%description
IP Tables State (iptstate) was originally written to implement 
the "state top" feature of IP Filter in IP Tables. "State top" 
displays the states held by your stateful firewall in a top-like 
manner.

Since IP Tables doesn't have a built in way to easily display 
this information even once, an option was added to just have it 
display the state table once.

  Features include:
        - Top-like realtime state table information
        - Sorting by any field
        - Reversible sorting
        - Single display of state table
        - Customizable refresh rate
        - Display filtering
        - Color-coding
        - Open Source
        - much more...

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=%{buildroot}%{_prefix} SBIN=%{buildroot}%{_sbindir}

%files
%doc LICENSE README.md
%{_sbindir}/iptstate
%{_mandir}/man8/iptstate.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.7-11
- Prepare for Oreon 11 (RP1)
