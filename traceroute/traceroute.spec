Summary: Traces the route taken by packets over an IPv4/IPv6 network
Name: traceroute
Epoch: 3
Version: 2.1.6
Release: 4%{?dist}
License: GPL-2.0-or-later
URL:  http://traceroute.sourceforge.net
Source0: https://downloads.sourceforge.net/project/traceroute/traceroute/traceroute-%{version}/traceroute-%{version}.tar.gz

Provides: tcptraceroute = 1.5-1
Obsoletes: tcptraceroute < 1.5-1

BuildRequires: make
BuildRequires: gcc


%description
The traceroute utility displays the route used by IP packets on their
way to a specified network (or Internet) host.  Traceroute displays
the IP number and host name (if possible) of the machines along the
route taken by the packets.  Traceroute is used as a network debugging
tool.  If you're having network connectivity problems, traceroute will
show you where the trouble is coming from along the route.

Install traceroute if you need a tool for diagnosing network connectivity
problems.


%prep
%setup -q


%build
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" SKIPDIRS="${RPM_SPECPARTS_DIR##*/}"


%install
install -D -p -m755 traceroute/traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute
ln -s traceroute $RPM_BUILD_ROOT%{_bindir}/traceroute6
install -D -p -m755 wrappers/tcptraceroute $RPM_BUILD_ROOT%{_bindir}/tcptraceroute
install -D -p -m644 traceroute/traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8/traceroute.8
ln -s traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8/traceroute6.8
ln -s traceroute.8 $RPM_BUILD_ROOT%{_mandir}/man8/tcptraceroute.8


%files
%license COPYING
%doc README TODO CREDITS
%{_bindir}/*
%{_mandir}/*/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.6-4
- Prepare for Oreon 11 (RP1)
