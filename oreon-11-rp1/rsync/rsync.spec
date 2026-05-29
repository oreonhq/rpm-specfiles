%global source0_hash none

%global _hardened_build 1

%define isprerelease 0

%if %isprerelease
%define prerelease pre3
%endif

Summary: A program for synchronizing files over a network
Name: rsync
Version: 3.4.1
Release: 6%{?prerelease}%{?dist}
URL: https://rsync.samba.org/

Source0:        https://download.samba.org/pub/rsync/src/rsync-3.4.1%{?prerelease}.tar.gz
Source1:        https://download.samba.org/pub/rsync/src/rsync-patches-3.4.1%{?prerelease}.tar.gz
Source2: rsyncd.socket
Source3: rsyncd.service
Source4: rsyncd.conf
Source5: rsyncd.sysconfig
Source6: rsyncd@.service

BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libacl-devel
BuildRequires: libattr-devel
BuildRequires: autoconf
BuildRequires: popt-devel
BuildRequires: systemd
BuildRequires: lz4-devel
BuildRequires: openssl-devel
BuildRequires: libzstd-devel
%if %{undefined rhel}
BuildRequires: xxhash-devel
%endif
#Added virtual provide for zlib due to https://fedoraproject.org/wiki/Bundled_Libraries?rd=Packaging:Bundled_Libraries
Provides: bundled(zlib) = 1.2.8
#rsync code is distributed under GPLv3+ license. There are files under popt/ directory
#which are provided under X11 license but they are not compiled. Except rsync links to
#popt provided by popt-devel from the system. Should this change, X11 license should be 
#mentioned here as well.
License: GPL-3.0-or-later

Patch1: rsync-3.2.2-runtests.patch
Patch2: rsync-3.4.1-rrsync-man.patch
Patch3: rsync-3.4.1-gcc15-fixes.patch
Patch4: rsync-3.4.1-cve-2025-10158.patch

%description
Rsync uses a reliable algorithm to bring remote and host files into
sync very quickly. Rsync is fast because it just sends the differences
in the files over the network instead of sending the complete
files. Rsync is often used as a very powerful mirroring process or
just as a more capable replacement for the rcp command. A technical
report which describes the rsync algorithm is included in this
package.

%package daemon
Summary: Service for anonymous access to rsync
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
%{?systemd_requires}
%description daemon
Rsync can be used to offer read only access to anonymous clients. This
package provides the anonymous rsync service.

%package rrsync
Summary: A script to setup restricted rsync users via ssh logins
BuildArch: noarch
Requires: %{name} = %{version}-%{release}
Requires: python3
%description rrsync
This subpackage provides rrsync script and its manpage. rrsync
may be used to setup a restricted rsync users via ssh logins.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
# TAG: for pre versions use

%if %isprerelease
%setup -q -n rsync-%{version}%{?prerelease}
%setup -q -b 1 -n rsync-%{version}%{?prerelease}
%else
%setup -q
%setup -q -b 1
%endif

%patch 1 -p1 -b .runtests
%patch 2 -p1 -b .rrsync

patch -p1 -i patches/detect-renamed.diff
patch -p1 -i patches/detect-renamed-lax.diff

%patch 3 -p1 -b .gcc15
%patch 4 -p1 -b .cve-2025-10158

%build
%configure \
  --enable-openssl \
%if %{defined rhel}
  --disable-xxhash \
%endif
  --enable-zstd \
  --enable-lz4 \
  --enable-ipv6 \
  --with-rrsync

%{make_build}

%check
make check
chmod -x support/*

%install
%{make_install} INSTALLCMD='install -p' INSTALLMAN='install -p'

install -D -m644 %{SOURCE3} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd.service
install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd.socket
install -D -m644 %{SOURCE4} $RPM_BUILD_ROOT/%{_sysconfdir}/rsyncd.conf
install -D -m644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/rsyncd
install -D -m644 %{SOURCE6} $RPM_BUILD_ROOT/%{_unitdir}/rsyncd@.service

%files
%license COPYING
%doc support/ tech_report.tex
%{_bindir}/%{name}
%{_bindir}/%{name}-ssl
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-ssl.1*
%{_mandir}/man5/rsyncd.conf.5*
%config(noreplace) %{_sysconfdir}/rsyncd.conf

%files daemon
%config(noreplace) %{_sysconfdir}/sysconfig/rsyncd
%{_unitdir}/rsyncd.socket
%{_unitdir}/rsyncd.service
%{_unitdir}/rsyncd@.service

%files rrsync
%{_bindir}/r%{name}
%{_mandir}/man1/r%{name}.1*

%post daemon
%systemd_post rsyncd.service

%preun daemon
%systemd_preun rsyncd.service

%postun daemon
%systemd_postun_with_restart rsyncd.service

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.1-6
- Prepare for Oreon 11 (RP1)
