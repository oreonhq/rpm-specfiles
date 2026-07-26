%global source0_hash a78e55a0df62b7f98566676d0ab9041aad89b2384bb5c6f3a96302a5cf49968d

Summary: Text mode Mail Client
Name: neomutt
Version: 20260105
Release: 2%{?dist}
Epoch: 6
Url: https://neomutt.org/

# Source, docs and contrib: GPLv2+, except for:
# BSD: Autosetup build system, queue.h
# MIT: Acutest unit test framework, some themes
# Public Domain: pgpewrap.c, mbox.5, some themes
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain

Source: https://github.com/neomutt/neomutt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: fedora-colors.rc

# Use system certificate bundle
Patch0: neomutt-system_certs.patch
# Use system ciphers (@SYSTEM)
Patch1: neomutt-ssl_ciphers.patch
# Temporary fix for autosetup
Patch2: neomutt-autosetup.patch

Requires: mailcap
Recommends: urlview

# Build NeoMutt
BuildRequires: cyrus-sasl-devel, gcc, gettext, gettext-devel, gnutls-devel
BuildRequires: gpgme-devel, krb5-devel, libidn2-devel, libzstd-devel
BuildRequires: lmdb-devel, lua-devel, lz4-devel, ncurses-devel, notmuch-devel
BuildRequires: pcre2-devel, sqlite-devel, tokyocabinet-devel, zlib-devel

# Generate Documentation
BuildRequires: /usr/bin/xsltproc, docbook-dtds, docbook-style-xsl, perl, lynx

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
NeoMutt is a small but very powerful text-based MIME mail client.  NeoMutt is
highly configurable, and is well suited to the mail power user with advanced
features like key bindings, keyboard macros, mail threading, regular expression
searches and a powerful pattern matching language for selecting groups of
messages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P 0 -p1 -b .system_certs
%patch -P 1 -p1 -b .ssl_ciphers
%patch -P 2 -p1 -b .autosetup

%build
%{configure} \
    CC=gcc \
    SENDMAIL=%{_sbindir}/sendmail \
    ISPELL=%{_bindir}/hunspell \
    --autocrypt --disable-idn --full-doc --gnutls --gpgme --gss --idn2 --lmdb \
    --lua --lz4 --notmuch --pcre2 --sasl --tokyocabinet --zlib --zstd

%{make_build}

# remove unique id in manual.html because multilib conflicts
sed -i -r 's/<a id="id[a-z0-9]\+">/<a id="id">/g' docs/manual.html

%install
%{make_install}
rm %{buildroot}%{_pkgdocdir}/INSTALL.md %{buildroot}%{_pkgdocdir}/LICENSE.md
cat %{SOURCE1} >> %{buildroot}%{_sysconfdir}/neomuttrc

%find_lang %{name}

%files -f %{name}.lang
%config(noreplace) %{_sysconfdir}/neomuttrc
%{_bindir}/neomutt
%{_libexecdir}/neomutt
%license LICENSE.md
%{_pkgdocdir}
%{_mandir}/man1/neomutt.*
%{_mandir}/man1/pgpewrap_neomutt.*
%{_mandir}/man1/smime_keys_neomutt.*
%{_mandir}/man5/mbox_neomutt.*
%{_mandir}/man5/mmdf_neomutt.*
%{_mandir}/man5/neomuttrc.*
%{_datadir}/neomutt

%changelog
%autochangelog
