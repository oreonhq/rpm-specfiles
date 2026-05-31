%global source0_hash 71ee3d1c3e107c93e082148f75ee460c949b203c861dd20d48f7c5cfdc272bf8

%global _hardened_build 1

Summary: A RFC 1413 ident protocol daemon
Name: authd
Version: 1.4.4
Release: 21%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/InfrastructureServices/authd
Obsoletes: pidentd < 3.2
Provides: pidentd = 3.2
Requires(post): openssl
Source0: https://github.com/InfrastructureServices/authd/releases/download/v1.4.4/authd-1.4.4.tar.gz
Source1: auth.socket
Source2: auth@.service
BuildRequires:  gcc
BuildRequires: openssl-devel gettext help2man systemd-units
BuildRequires: make
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
authd is a small and fast RFC 1413 ident protocol daemon
with both xinetd server and interactive modes that
supports IPv6 and IPv4 as well as the more popular features
of pidentd.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup

%build
make prefix=%{_prefix} CFLAGS="%{optflags}" \
        LDFLAGS="-lcrypto %{build_ldflags}"


%install
%make_install datadir=%{buildroot}/%{_datadir} \
	sbindir=%{buildroot}/%{_sbindir}

install -d %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/

install -d %{buildroot}%{_sysconfdir}/
touch %{buildroot}%{_sysconfdir}/ident.key

install -d %{buildroot}/%{_mandir}/man1/
help2man -N -v -V %{buildroot}/%{_sbindir}/in.authd -o \
         %{buildroot}/%{_mandir}/man1/in.authd.1

%find_lang %{name}

%post
/usr/sbin/adduser -s /sbin/nologin -u 98 -r -d '/' ident 2>/dev/null || true
/usr/bin/openssl rand -base64 -out %{_sysconfdir}/ident.key 32
echo CHANGE THE LINE ABOVE TO A PASSPHRASE >> %{_sysconfdir}/ident.key
/bin/chown ident:ident %{_sysconfdir}/ident.key
chmod o-rw %{_sysconfdir}/ident.key
%systemd_post auth.socket

%postun
%systemd_postun_with_restart auth.socket

%preun
%systemd_preun auth.socket

%files -f authd.lang
%license COPYING
%verify(not md5 size mtime user group) %config(noreplace) %attr(640,root,root) %{_sysconfdir}/ident.key
%doc COPYING README.html rfc1413.txt
%{_sbindir}/in.authd
%{_mandir}/*/*
%{_unitdir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.4-21
- Prepare for Oreon 11 (RP1)
