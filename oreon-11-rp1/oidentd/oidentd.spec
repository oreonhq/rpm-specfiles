%global source0_hash feaa1f5e23df9a0a6b351bffd75345d575a209d5908f60cb3aaf4349f38cb0b0

# Regenerate documentation with asciidoctor
%bcond_without  oidentd_enables_asciidoctor
Summary:    RFC 1413-compliant identification server with NAT support
Name:       oidentd
Version:    3.1.0
Release:    10%{?dist}
# COPYING:                  GPL-2.0 text
# COPYING.DOC:              GFDL-1.3 text
# doc/book/src/download.md:                                 GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/capabilities.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/configuration/index.md:      GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/configuration/examples.md:   GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/index.md:                    GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/installation.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/starting-the-server.md:      GFDL-1.3-no-invariants-or-later
# doc/book/src/getting-started/support.md:                  GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/index.md:                             GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/using-oidentd-with-quassel.md:        GFDL-1.3-no-invariants-or-later
# doc/book/src/guides/using-oidentd-with-znc.md:            GFDL-1.3-no-invariants-or-later
# doc/book/src/index.md:                                    GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/forwarding.md:                           GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/index.md:                                GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/introduction.md:                         GFDL-1.3-no-invariants-or-later
# doc/book/src/nat/static-replies.md:                       GFDL-1.3-no-invariants-or-later
# doc/book/src/security/dropping-privileges.md:             GFDL-1.3-no-invariants-or-later
# doc/book/src/security/hiding-connections.md:              GFDL-1.3-no-invariants-or-later
# doc/book/src/security/identification-vs-authentication.md:    GFDL-1.3-no-invariants-or-later
# doc/book/src/security/index.md:                           GFDL-1.3-no-invariants-or-later
# doc/book/src/SUMMARY.md:  GFDL-1.3-no-invariants-or-later
# doc/oidentd.8:            GFDL-1.3-no-invariants-or-later
# doc/oidentd.8.adoc:       GFDL-1.3-no-invariants-or-later
# doc/oidentd.conf.5.adoc:  GFDL-1.3-no-invariants-or-later
# doc/oidentd_masq.conf.5:  GFDL-1.3-no-invariants-or-later
# doc/oidentd_masq.conf.5.adoc  GFDL-1.3-no-invariants-or-later
# src/cfg_scan.l:           GPL-2.0-only
# src/forward.c:            GPL-2.0-only
# src/forward.h:            GPL-2.0-only
# src/inet_util.c:          GPL-2.0-only
# src/inet_util.h:          GPL-2.0-only
# src/oidentd.c:            GPL-2.0-only
# src/oidentd.h:            GPL-2.0-only
# src/options.c:            GPL-2.0-only
# src/options.h:            GPL-2.0-only
# src/masq.c:               GPL-2.0-only
# src/masq.h:               GPL-2.0-only
# src/missing/missing.h:    GPL-2.0-only
# src/netlink.h:            GPL-2.0-only
# src/os.c:                 GPL-2.0-only
# src/user_db.c:            GPL-2.0-only
# src/user_db.h:            GPL-2.0-only
# src/util.c:               GPL-2.0-only
# src/util.h:               GPL-2.0-only
## Files unbundled
# src/cfg_parse.c:          GPL-3.0-or-later WITH Bison-exception-2.2
#                           AND GPL-2.0-only (derived from src/cfg_parse.y)
# src/cfg_parse.h:          GPL-3.0-or-later WITH Bison-exception-2.2
#                           AND GPL-2.0-only (derived from src/cfg_parse.y)
# src/cfg_scan.c:           GPL-2.0-only
# src/missing/inet_aton.c:  BSD-4-Clause-UC AND MIT-like (completely hidden by HAVE_INET_ATON macro)
# src/missing/ipv6_missing.c:   BSD-2-Clause
# src/missing/getopt.c:     LGPL-2.1-or-later (bundled from glibc)
# src/missing/getopt_missing.h: LGPL-2.1-or-later (bundled from glibc)
# src/missing/vasprintf.c:  LGPL-2.0-or-later (bundled from libiberty)
## Files not in a binary package
# aclocal.m4:               FSFULLRWD
# ar-lib:                   GPL-2.0-or-later WITH Autoconf-exception-generic
# compile:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# config.sub:               GPL-3.0-or-later WITH Autoconf-exception-generic
# config.guess:             GPL-3.0-or-later WITH Autoconf-exception-generic
# configure:                FSFUL
# configure.ac:             GPL-2.0-only
# depcomp:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# doc/Makefile.in:          FSFULLRWD
# INSTALL:                  FSFAP
# install-sh:               X11 AND LicenseRef-Fedora-Public-Domain
# Makefile.in:              FSFULLRWD
# missing:                  GPL-2.0-or-later WITH Autoconf-exception-generic
# src/missing/getopt_missing.h:     LGPL-2.1-or-later (bundled from glibc)
# src/kernel/dflybsd1.c:    GPL-2.0-only
# src/kernel/netbsd5.c:     GPL-2.0-only
# src/kernel/openbsd30.c:   GPL-2.0-only
# ylwrap:                   GPL-2.0-or-later WITH Autoconf-exception-generic
License:    GPL-2.0-only AND GFDL-1.3-no-invariants-or-later
URL:        https://%{name}.janikrabe.com/
Source0:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz
Source1:    https://files.janikrabe.com/pub/%{name}/releases/%{version}/%{name}-%{version}.tar.xz.asc
Source2:    https://files.janikrabe.com/keys/63694DD76ED116B84D286F75C4CD3CE186D1CA13.asc
Source3:    oidentd.service
Source4:    oidentd.sysconfig
# Use sysconfig options in a per-connection unit file, not suitable for
# the upstream
Patch0:     oidentd-3.1.0-Make-per-connection-unit-file-similar-to-Fedora-long.patch
Patch1:     oidentd-configure-c-compatibility.patch
BuildRequires:  autoconf
BuildRequires:  automake
# ylwrap script is a sh script
BuildRequires:  bash
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libnetfilter_conntrack-devel
BuildRequires:  make
%if %{with oidentd_enables_asciidoctor}
# asciidoctor regenerates the documentation
BuildRequires:  rubygem-asciidoctor
%endif
# sed called by ylwrap
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):  shadow-utils
%endif
Provides:       identd = %{version}-%{release}

%description
The oidentd package contains identd, which implements the RFC 1413
identification server.  Identd looks up specific TCP/IP connections
and returns either the user name or other information about the
process that owns the connection.

Install oidentd if you need to look up information about specific
TCP/IP connections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Replace files whose code is excluded from compilation by a C preprocessor
# macro but whose license would influence a license of the executable.
truncate -c -s 0 src/missing/getopt.c
truncate -c -s 0 src/missing/getopt_missing.h
truncate -c -s 0 src/missing/inet_aton.c
truncate -c -s 0 src/missing/ipv6_missing.c
truncate -c -s 0 src/missing/vasprintf.c
# Regenerate files
rm src/cfg_parse.{c,h}
rm src/cfg_scan.c
%if %{with oidentd_enables_asciidoctor}
rm doc/*.{5,8}
%endif
# Remove VCS files
rm doc/book/.gitignore

# Create a sysusers.d config file
cat >oidentd.sysusers <<EOF
u oidentd - 'oidentd daemon' - -
EOF

%build
autoreconf -fi
%configure \
    --disable-debug \
    --enable-ipv6 \
    --enable-libnfct \
    --enable-nat \
    --disable-warn \
    --enable-xdgbdir
%{make_build}

%install
%{make_install}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/oidentd.service
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/oidentd
install -D -p -m 0644 contrib/systemd/oidentd.socket %{buildroot}%{_unitdir}/
install -D -p -m 0644 contrib/systemd/oidentd\@.service %{buildroot}%{_unitdir}/
install -m0644 -D oidentd.sysusers %{buildroot}%{_sysusersdir}/oidentd.conf

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre
getent group oidentd >/dev/null || groupadd -r oidentd
getent passwd oidentd >/dev/null || \
    useradd -r -g oidentd -d / -s /sbin/nologin -c "oidentd daemon" oidentd
exit 0
%endif

%post
%systemd_post oidentd.service

%preun
%systemd_preun oidentd.service

%postun
%systemd_postun_with_restart oidentd.service

%files
%license COPYING*
%doc AUTHORS ChangeLog doc/book KERNEL_SUPPORT.md NEWS README
%config(noreplace) %{_sysconfdir}/oidentd.conf
%config(noreplace) %{_sysconfdir}/oidentd_masq.conf
%config(noreplace) %{_sysconfdir}/sysconfig/oidentd
%dir %{_prefix}/lib/systemd
%dir %{_unitdir}
%{_unitdir}/oidentd.service
%{_unitdir}/oidentd@.service
%{_unitdir}/oidentd.socket
%{_sbindir}/oidentd
%{_mandir}/man5/oidentd*
%{_mandir}/man8/oidentd.*
%{_sysusersdir}/oidentd.conf

%changelog
%autochangelog
