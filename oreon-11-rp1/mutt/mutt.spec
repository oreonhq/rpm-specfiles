%global source0_hash 2703ff1a51a99c3163d4fd998ac22e982bbd5493d512a7c5bde716a8adba0394
%bcond_without debug
%bcond_without imap
%bcond_without pop
%bcond_without smtp
%bcond_without gnutls
%bcond_without gss
%bcond_without sasl
%bcond_with idn
%bcond_without idn2
%bcond_without hcache
%bcond_without tokyocabinet
%bcond_with bdb
%bcond_with qdbm
%bcond_with gdbm
%bcond_without gpgme
%bcond_without sidebar
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        A text mode mail user agent
Name: mutt
Version: 2.4.2
Release:        1%{?dist}
Epoch: 5
License: GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
Source0:        http://ftp.mutt.org/pub/%{name}/%{name}-%{version}.tar.gz
Source1: mutt_ldap_query
Patch1: mutt-1.10.0-muttrc.patch
Patch2: mutt-1.8.0-cabundle.patch
Patch8: mutt-1.5.23-system_certs.patch
Patch9: mutt-1.9.0-ssl_ciphers.patch
Patch10: mutt-1.9.4-lynx_no_backscapes.patch
Patch12: mutt-1.9.5-nodotlock.patch
Patch13: mutt-1.12.1-optusegpgagent.patch
Url: http://www.mutt.org
Requires: mailcap, urlview
%if %{with hcache}
%{?with_tokyocabinet:BuildRequires: tokyocabinet-devel}
%{?with_bdb:BuildRequires: db4-devel}
%{?with_qdbm:BuildRequires: qdbm-devel}
%{?with_gdbm:BuildRequires: gdbm-devel}
%endif
%if %{with imap} || %{with pop} || %{with smtp}
%{?with_gnutls:BuildRequires: gnutls-devel}
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%endif
%if %{with imap}
%{?with_gss:BuildRequires: krb5-devel}
%endif
%{?with_idn:BuildRequires: libidn-devel}
%{?with_idn2:BuildRequires: libidn2-devel}
%{?with_gpgme:BuildRequires: gpgme-devel}
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  db4-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  krb5-devel
BuildRequires:  libidn2-devel
BuildRequires:  lynx
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  tokyocabinet-devel
# /oreon:deps
%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# unpack; cd
%setup -q
# do not run ./prepare -V, because it also runs ./configure

%patch -P10 -p1 -b .lynx_no_backscapes
%patch -P12 -p1 -b .nodotlock

autoreconf -fiv
%patch -P1 -p1 -b .muttrc
%patch -P2 -p1 -b .cabundle
%patch -P8 -p1 -b .system_certs
%patch -P9 -p1 -b .ssl_ciphers
%patch -P13 -p1 -b .optusegpgagent

sed -i -r 's/`$GPGME_CONFIG --libs`/"\0 -lgpg-error"/' configure

install -p -m644 %{SOURCE1} mutt_ldap_query

%global hgreldate \\.(201[0-9])([0-1][0-9])([0-3][0-9])hg
if echo %{release} | grep -E -q '%{hgreldate}'; then
  echo -n 'const char *ReleaseDate = ' > reldate.h
  echo %{release} | sed -r 's/.*%{hgreldate}.*/"\1-\2-\3";/' >> reldate.h
fi

# remove mutt_ssl.c to be sure it won't be used because it violates
# Packaging:CryptoPolicies
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
rm -f mutt_ssl.c

%build

%configure \
    SENDMAIL=%{_sbindir}/sendmail \
    ISPELL=%{_bindir}/hunspell \
    %{?with_debug:	--enable-debug}\
    %{?with_pop:	--enable-pop}\
    %{?with_imap:	--enable-imap} \
    %{?with_smtp:	--enable-smtp} \
\
    %if %{with hcache}
    --enable-hcache \
    %{!?with_tokyocabinet:	--without-tokyocabinet} \
    %{!?with_gdbm:	--without-gdbm} \
    %{!?with_qdbm:	--without-qdbm} \
    %endif
\
    %if %{with imap} || %{with pop} || %{with smtp}
    %{?with_gnutls:	--with-gnutls} \
    %{?with_sasl:	--with-sasl} \
    %endif
\
    %if %{with imap}
    %{?with_gss:	--with-gss} \
    %endif
\
    %{?with_idn:	--with-idn} \
    %{!?with_idn:	--without-idn} \
    %{?with_idn2:   --with-idn2} \
    %{!?with_idn2:  --without-idn2} \
\
    %{?with_gpgme:	--enable-gpgme} \
    %{?with_sidebar: --enable-sidebar} \
    --with-docdir=%{_pkgdocdir}
%make_build
sed -i -r 's/<a id="id[a-z0-9]\+">/<a id="id">/g' doc/manual.html
oauth2_script="contrib/mutt_oauth2.py"
t=$(stat -c %y "${oauth2_script}")
sed -i "s:^#\!/usr/bin/env\s\+python3\s\?$:#!%{python3}:" "${oauth2_script}"
touch -d "$t" "${oauth2_script}"
%install
%make_install
cat contrib/gpg.rc >> \
      %{buildroot}%{_sysconfdir}/Muttrc
grep -5 "^color" contrib/sample.muttrc >> \
      %{buildroot}%{_sysconfdir}/Muttrc
cat >> %{buildroot}%{_sysconfdir}/Muttrc <<\EOF
source %{_sysconfdir}/Muttrc.local
EOF
echo "# Local configuration for Mutt." > \
      %{buildroot}%{_sysconfdir}/Muttrc.local
rm -f %{buildroot}%{_sysconfdir}/*.dist
rm -f %{buildroot}%{_sysconfdir}/mime.types
rm -f %{buildroot}%{_bindir}/mutt_dotlock
rm -f %{buildroot}%{_bindir}/muttbug
rm -f %{buildroot}%{_bindir}/flea
rm -f %{buildroot}%{_mandir}/man1/mutt_dotlock.1*
rm -f %{buildroot}%{_mandir}/man1/muttbug.1*
rm -f %{buildroot}%{_mandir}/man1/flea.1*
rm -f %{buildroot}%{_mandir}/man5/mbox.5*
rm -f %{buildroot}%{_mandir}/man5/mmdf.5*
rm -rf %{buildroot}%{_pkgdocdir}
rm -f %{buildroot}%{_infodir}/dir
ln -sf ./muttrc.5 %{buildroot}%{_mandir}/man5/muttrc.local.5
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
