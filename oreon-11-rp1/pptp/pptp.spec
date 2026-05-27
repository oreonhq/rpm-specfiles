%global source0_hash 82492db8e487ce73b182ee7f444251d20c44f5c26d6e96c553ec7093aefb5af4

Name:		pptp
Version:	1.10.0
Release:	24%{?dist}
Summary:	Point-to-Point Tunneling Protocol (PPTP) Client
License:	gpl-2.0-or-later
URL:		http://pptpclient.sourceforge.net/
Source0:	http://downloads.sf.net/pptpclient/pptp-%{version}.tar.gz
Source1:	pptp-tmpfs.conf
BuildRequires:	make
BuildRequires:	/usr/bin/pod2man
BuildRequires:	gcc, perl-generators
Requires:	ppp >= 2.4.2, /sbin/ip
Requires:	systemd-units
# Patch sent upstream
Patch0:		pptp-1.10.0-man-fix.patch

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP. Allows connection to a PPTP based VPN as used
by employers and some cable and ADSL service providers.

%package setup
Summary:	PPTP Tunnel Configuration Script
Requires:	%{name} = %{version}-%{release}

%description setup
This package provides a simple configuration script for setting up PPTP
tunnels.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%patch -P0 -p1 -b .man-fix

# Pacify rpmlint
perl -pi -e 's/install -o root -m 555 pptp/install -m 755 pptp/;' Makefile

%build
OUR_CFLAGS="-Wall %{optflags} -Wextra -Wstrict-aliasing=2 -Wnested-externs -Wstrict-prototypes"
%{make_build} CFLAGS="$OUR_CFLAGS" LDFLAGS="$RPM_LD_FLAGS" IP=/sbin/ip

%install
rm -rf %{buildroot}
%{make_install} DESTDIR=%{buildroot} BINDIR=%{buildroot}%{_sbindir}
install -d -m 750 %{buildroot}%{_localstatedir}/run/pptp


install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
install -p -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/tmpfiles.d/pptp.conf

%files
%doc AUTHORS COPYING DEVELOPERS NEWS README TODO USING
%doc ChangeLog Documentation/DESIGN.PPTP PROTOCOL-SECURITY
%{_prefix}/lib/tmpfiles.d/pptp.conf
%{_sbindir}/pptp
%{_mandir}/man8/pptp.8*
%dir %attr(750,root,root) %{_localstatedir}/run/pptp/
%config(noreplace) %{_sysconfdir}/ppp/options.pptp

%files setup
%{_sbindir}/pptpsetup
%{_mandir}/man8/pptpsetup.8*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.0-24
- Prepare for Oreon 11 (RP1)
