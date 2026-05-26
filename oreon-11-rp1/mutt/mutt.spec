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

Summary: A text mode mail user agent
Name: mutt
Version: 2.3.0
Release: 1%{?dist}
Epoch: 5
# The entire source code is GPLv2+ except
# pgpewrap.c setenv.c sha1.c wcwidth.c which are Public Domain
License: GPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain
# hg snapshot created from http://dev.mutt.org/hg/mutt
Source: http://ftp.mutt.org/pub/%{name}/%{name}-%{version}.tar.gz
Source1: mutt_ldap_query
Patch1: mutt-1.10.0-muttrc.patch
Patch2: mutt-1.8.0-cabundle.patch
# https://dev.mutt.org/trac/ticket/3569
Patch3: mutt-1.7.0-syncdebug.patch
# FIXME make it to upstream
Patch8: mutt-1.5.23-system_certs.patch
Patch9: mutt-1.9.0-ssl_ciphers.patch
Patch10: mutt-1.9.4-lynx_no_backscapes.patch
Patch12: mutt-1.9.5-nodotlock.patch
Patch13: mutt-1.12.1-optusegpgagent.patch
# oreon url source checksums begin
%global source0_sha256 5d5ebc40843f7156d5ede30e50016798ac7336467f7ad347e716510516cc2130
%global source0_file mutt-2.3.0.tar.gz
# oreon url source checksums end

Url: http://www.mutt.org
Requires: mailcap, urlview
BuildRequires: make
BuildRequires: gcc
BuildRequires: ncurses-devel, gettext, automake
# manual generation
BuildRequires: /usr/bin/xsltproc, docbook-style-xsl, perl-interpreter
BuildRequires: perl-generators
BuildRequires: lynx

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


%description
Mutt is a small but very powerful text-based MIME mail client.  Mutt
is highly configurable, and is well suited to the mail power user with
advanced features like key bindings, keyboard macros, mail threading,
regular expression searches and a powerful pattern matching language
for selecting groups of messages.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/mutt-2.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "5d5ebc40843f7156d5ede30e50016798ac7336467f7ad347e716510516cc2130" || { echo "oreon: Source0 SHA256 mismatch for mutt-2.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
# unpack; cd
%setup -q
# do not run ./prepare -V, because it also runs ./configure

%patch -P10 -p1 -b .lynx_no_backscapes
%patch -P12 -p1 -b .nodotlock

autoreconf -fiv
%patch -P1 -p1 -b .muttrc
%patch -P2 -p1 -b .cabundle
%patch -P3 -p1 -b .syncdebug
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

# remove unique id in manual.html because multilib conflicts
sed -i -r 's/<a id="id[a-z0-9]\+">/<a id="id">/g' doc/manual.html

# fix the shebang in mutt_oauth2.py & preserve the time stamp
oauth2_script="contrib/mutt_oauth2.py"
t=$(stat -c %y "${oauth2_script}")
sed -i "s:^#\!/usr/bin/env\s\+python3\s\?$:#!%{python3}:" "${oauth2_script}"
touch -d "$t" "${oauth2_script}"

%install
%make_install

# we like GPG here
cat contrib/gpg.rc >> \
      %{buildroot}%{_sysconfdir}/Muttrc

grep -5 "^color" contrib/sample.muttrc >> \
      %{buildroot}%{_sysconfdir}/Muttrc

cat >> %{buildroot}%{_sysconfdir}/Muttrc <<\EOF
source %{_sysconfdir}/Muttrc.local
EOF

echo "# Local configuration for Mutt." > \
      %{buildroot}%{_sysconfdir}/Muttrc.local

# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_sysconfdir}/*.dist
rm -f %{buildroot}%{_sysconfdir}/mime.types
# disable mutt_dotlock program - remove the compiled binary
rm -f %{buildroot}%{_bindir}/mutt_dotlock
rm -f %{buildroot}%{_bindir}/muttbug
rm -f %{buildroot}%{_bindir}/flea
rm -f %{buildroot}%{_mandir}/man1/mutt_dotlock.1*
rm -f %{buildroot}%{_mandir}/man1/muttbug.1*
rm -f %{buildroot}%{_mandir}/man1/flea.1*
rm -f %{buildroot}%{_mandir}/man5/mbox.5*
rm -f %{buildroot}%{_mandir}/man5/mmdf.5*
rm -rf %{buildroot}%{_pkgdocdir}

# remove /usr/share/info/dir
rm -f %{buildroot}%{_infodir}/dir

# provide muttrc.local(5): the same as muttrc(5)
ln -sf ./muttrc.5 %{buildroot}%{_mandir}/man5/muttrc.local.5

%find_lang %{name}


%files -f %{name}.lang
%{!?_licensedir:%global license %doc}
%license COPYRIGHT GPL
%doc ChangeLog NEWS README* UPDATING mutt_ldap_query
%doc contrib/mutt_oauth2.py contrib/mutt_oauth2.py.README
%doc contrib/*.rc contrib/sample.* contrib/colors.*
%doc doc/manual.html doc/manual.txt doc/smime-notes.txt
%config(noreplace) %{_sysconfdir}/Muttrc
%config(noreplace) %{_sysconfdir}/Muttrc.local
%{_bindir}/mutt
%{_bindir}/mutt_pgpring
%{_bindir}/pgpewrap
%{_bindir}/smime_keys
%{_mandir}/man1/mutt.*
%{_mandir}/man1/smime_keys.*
%{_mandir}/man1/mutt_pgpring.*
%{_mandir}/man1/pgpewrap.*
%{_mandir}/man5/muttrc.*
%{_infodir}/mutt.info.*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.0-1
- Prepare for Oreon 11 (RP1)
