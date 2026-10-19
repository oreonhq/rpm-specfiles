%global source1_hash 9c6423f0aac0e0a1a6afceaf05cee3125309960f7f2d3509c93a99494e8d33a4
%global source0_hash 8e7438ccd6b3a2ab05182d0846e112a56a7f557ecdee40de07bf67820008bef7
%global __provides_exclude_from ^%{_libdir}/stunnel/.*$
%if 0%{?fedora} || 0%{?rhel} > 7 || (0%{?oreon} >= 11)
%bcond_with libwrap
%else
%bcond_without libwrap
%endif
%if 0%{?rhel} >= 10 || (0%{?oreon} >= 11)
%bcond openssl_engine 0
%else
%bcond openssl_engine 1
%endif
Summary:        A TLS-encrypting socket wrapper
Name: stunnel
Version: 5.82
Release:        1%{?dist}
License: GPL-2.0-or-later WITH stunnel-exception AND MIT
URL: https://www.stunnel.org/
Source0:        https://www.stunnel.org/downloads/stunnel-%{version}.tar.gz
Source1:        https://www.stunnel.org/downloads/stunnel-%{version}.tar.gz.asc
Source2: Certificate-Creation
Source3: sfinger.xinetd
Source4: stunnel-sfinger.conf
Source5: pop3-redirect.xinetd
Source6: stunnel-pop3s-client.conf
Source7: stunnel@.service
Source99: pgp.asc
Patch0:   stunnel-5.50-authpriv.patch
Patch3:   stunnel-5.69-system-ciphers.patch
Patch5:   stunnel-5.72-default-tls-version.patch
%if %{with openssl_engine} && 0%{?fedora} >= 41 || (0%{?oreon} >= 11)
%endif
%if %{with libwrap}
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  /usr/bin/lsof
BuildRequires:  /usr/bin/nc
BuildRequires:  /usr/bin/ps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  pandoc
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-cryptography
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  util-linux
# /oreon:deps
%description
Stunnel is a socket wrapper which can provide TLS/SSL
(Transport Layer Security/Secure Sockets Layer) support
to ordinary applications. For example, it can be used in
conjunction with imapd to create a TLS secure IMAP server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE99}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S gendiff -p1

%build

CFLAGS="$RPM_OPT_FLAGS -fPIC"; export CFLAGS
if pkg-config openssl ; then
	CFLAGS="$CFLAGS `pkg-config --cflags openssl`";
	LDFLAGS="`pkg-config --libs-only-L openssl`"; export LDFLAGS
fi
CPPFLAGS_NO_ENGINE=""
%if !%{with openssl_engine}
	CPPFLAGS_NO_ENGINE="-DOPENSSL_NO_ENGINE"
%endif
%configure --enable-fips --enable-ipv6 --with-ssl=%{_prefix} \
%if %{with libwrap}
--enable-libwrap \
%else
--disable-libwrap \
%endif
	--with-bashcompdir=%{_datadir}/bash-completion/completions \
	CPPFLAGS="-UPIDFILE -DPIDFILE='\"%{_localstatedir}/run/stunnel.pid\"' $CPPFLAGS_NO_ENGINE"
make V=1 LDADD="-pie -Wl,-z,defs,-z,relro,-z,now"
%install
make install DESTDIR=%{buildroot}
for lang in pl ; do
	mkdir -p %{buildroot}/%{_mandir}/${lang}/man8
	mv %{buildroot}/%{_mandir}/man8/*.${lang}.8* %{buildroot}/%{_mandir}/${lang}/man8/
	rename ".${lang}" "" %{buildroot}/%{_mandir}/${lang}/man8/*
done
mkdir srpm-docs
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} srpm-docs
mkdir -p %{buildroot}%{_unitdir}
cp %{buildroot}%{_datadir}/doc/stunnel/examples/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
cp %{SOURCE7} %{buildroot}%{_unitdir}/%{name}@.service
%oreon_autofiles main

%check

if ! make test; then
	for i in tests/logs/*.log; do
		echo "$i":
		cat "$i"
	done
	exit 1
fi
%post

/sbin/ldconfig
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

/sbin/ldconfig
%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
