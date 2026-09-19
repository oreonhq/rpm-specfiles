%global source0_hash 02f5045de975d3a3e67ee32025d631696af0d4d80483f1088e6bfbd5ff66f428

# Use sysusers from Fedora 43 onwards
%if (0%{?rhel} && 0%{?rhel} <= 10) || (0%{?fedora} && 0%{?fedora} <= 42)
%global use_sysusers 0
%else
%global use_sysusers 1
%endif

Summary:		Milter for greylisting, the next step in the spam control war
Name:			milter-greylist
Version:		4.6.4
Release:		20%{?dist}
# License is like BSD-4-Clause but without the 4th clause
# We use spamd.c but not queue.h
# See READNE for details
License:		LicenseRef-Callaway-BSD-with-advertising
URL:			http://hcpnet.free.fr/milter-greylist/
Source0:		ftp://ftp.espci.fr/pub/milter-greylist/milter-greylist-%{version}.tgz
Source1:		README.fedora
Source20:		milter-greylist.systemd.service
Patch0:			milter-greylist-4.6.3-config.patch
Patch1:			milter-greylist-4.4.2-utf8.patch
Patch2:			milter-greylist-4.5.11-warning.patch
Patch4:			ai_addrconfig.patch
BuildRequires:		bison
BuildRequires:		coreutils
BuildRequires:		curl-devel
BuildRequires:		flex
BuildRequires:		gcc
BuildRequires:		libmaxminddb-devel
BuildRequires:		libspf2-devel
BuildRequires:		m4
BuildRequires:		make
BuildRequires:		perl-interpreter
BuildRequires:		sed
BuildRequires:		sendmail-milter-devel

# Scriptlet dependencies
BuildRequires:		systemd
%if !%{use_sysusers}
Requires(pre):		shadow-utils
%endif
%{?systemd_requires}

# Dependencies
Recommends:		geolite2-country

%description
Greylisting is a new method of blocking significant amounts of spam at
the mailserver level, but without resorting to heavyweight statistical
analysis or other heuristical (and error-prone) approaches. Consequently,
implementations are fairly lightweight, and may even decrease network
traffic and processor load on your mailserver.

This package provides a greylist filter for sendmail's milter API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n milter-greylist-%{version}

# Customize config for Fedora / EPEL
# * Specify pidfile in initscript rather than config file
# * Specify socket in config file rather than initscript
# * Specify grmilter as the user to run the dæmon as
# * Specify the GeoIP2 database location
%patch -P0

# Re-code docs as UTF8
%patch -P1

# Work around warning about _BSD_SOURCE being deprecated in favor
# of _DEFAULT_SOURCE breaking build due to use of -Werror
%patch -P2

# Work around issues with ISC libbind and AI_ADDRCONFIG
# http://tech.groups.yahoo.com/group/milter-greylist/message/5048
%patch -P4 -p1

# README.fedora
install -p -m 644 %{SOURCE1} .

# Don't let the configure script find libresolv
sed -i -e 's!/libresolv.a!/../../../no-such-lib.a!g' configure

# Set socket/db/pidfile to be in FHS-compliant places
for i in `find -type f`; do
    sed -e 's|/var/milter-greylist/milter-greylist.sock|/run/milter-greylist/milter-greylist.sock|g;
	    s|/var/milter-greylist/greylist.db|%{_localstatedir}/lib/milter-greylist/db/greylist.db|g;
	    s|/var/milter-greylist/milter-greylist.pid|/run/milter-greylist.pid|g;
	   ' "$i" >"$i.tmp"
    cmp -s "$i" "$i.tmp" || cat "$i.tmp" >"$i"
    rm -f "$i".tmp
done

# Create a sysusers.d config file
cat >milter-greylist.sysusers.conf <<EOF
u grmilter - 'Greylist-milter user' %{_localstatedir}/lib/milter-greylist -
EOF

%build
# Harden the build if supported
%global _hardened_build 1
export CFLAGS="%{__global_cflags} -fno-strict-aliasing -D_GNU_SOURCE -DSM_CONF_STDBOOL_H=1"
export LDFLAGS="-Wl,-z,now -Wl,-z,relro %{__global_ldflags} -Wl,--as-needed $LDLIBS"
%configure \
	--disable-drac				\
	--disable-rpath				\
	--enable-dnsrbl				\
	--enable-p0f				\
	--enable-spamassassin			\
	--with-drac-db=%{_localstatedir}/lib/milter-greylist/drac/drac.db \
	--with-libcurl				\
	--with-libmaxminddb			\
	--with-libspf2				\
	--with-user=grmilter

%{make_build} BINDIR=%{_sbindir}

%install
install -d -m 755 %{buildroot}{/run/milter-greylist,%{_localstatedir}/lib/milter-greylist/db}
%{make_install} \
	BINDIR=%{_sbindir} \
	TEST=false \
	USER="$(id -u)"

# Create a dummy socket so we can %%ghost it and remove it on uninstall
touch %{buildroot}/run/milter-greylist/milter-greylist.sock

# sysusers config
%if %{use_sysusers}
install -m0644 -D milter-greylist.sysusers.conf %{buildroot}%{_sysusersdir}/milter-greylist.conf
%endif

# Initscript
install -D -p -m 0644 %{SOURCE20} %{buildroot}%{_unitdir}/milter-greylist.service

# Make sure /run/milter-greylist is re-created at boot time if /run is on tmpfs
install -d -m 755 %{buildroot}%{_prefix}/lib/tmpfiles.d
cat << EOF > %{buildroot}%{_prefix}/lib/tmpfiles.d/milter-greylist.conf
d /run/milter-greylist 0710 root mail
EOF

%if !%{use_sysusers}
%pre
# Create account for milter-greylist to run as
getent group grmilter >/dev/null || groupadd -r grmilter
getent passwd grmilter >/dev/null || \
	useradd -r -g grmilter -d %{_localstatedir}/lib/milter-greylist -s /sbin/nologin \
	 -c "Greylist-milter user" grmilter
exit 0
%endif

%post
%systemd_post milter-greylist.service

%preun
%systemd_preun milter-greylist.service

%postun
%systemd_postun_with_restart milter-greylist.service

%files
%license README
%doc ChangeLog README.fedora milter-greylist.m4
%{_sbindir}/milter-greylist
%attr(0640,root,grmilter) %verify(not mtime) %config(noreplace) %{_sysconfdir}/mail/greylist.conf
%dir %attr(0751,grmilter,grmilter) %{_localstatedir}/lib/milter-greylist/
%dir %attr(0770,root,grmilter) %{_localstatedir}/lib/milter-greylist/db/
%dir %attr(0710,root,mail) /run/milter-greylist/
%{_mandir}/man5/greylist.conf.5*
%{_mandir}/man8/milter-greylist.8*
%ghost /run/milter-greylist/milter-greylist.sock
%{_prefix}/lib/tmpfiles.d/milter-greylist.conf
%if %{use_sysusers}
%{_sysusersdir}/milter-greylist.conf
%endif
%{_unitdir}/milter-greylist.service

%changelog
%autochangelog
