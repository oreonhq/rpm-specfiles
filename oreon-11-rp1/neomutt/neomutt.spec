%global source0_hash 2c34fdd2166d5765e6bfdc21d1248bc4e92ddc0a33537b9418c17cd90e2dda80
Summary:        Text mode Mail Client
Name: neomutt
Version: 20260616
Release:        1%{?dist}
Epoch: 6
Url: https://neomutt.org/
License: GPL-2.0-or-later AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-Public-Domain
Source0:        https://github.com/neomutt/neomutt/archive/%{version}/%{name}-%{version}.tar.gz
Source1: fedora-colors.rc
Patch0: neomutt-system_certs.patch
Patch1: neomutt-ssl_ciphers.patch
Patch2: neomutt-autosetup.patch
Requires: mailcap
Recommends: urlview
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  cyrus-sasl-devel
BuildRequires:  docbook-dtds
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  krb5-devel
BuildRequires:  libidn2-devel
BuildRequires:  libzstd-devel
BuildRequires:  lmdb-devel
BuildRequires:  lua-devel
BuildRequires:  lynx
BuildRequires:  lz4-devel
BuildRequires:  ncurses-devel
BuildRequires:  notmuch-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  sqlite-devel
BuildRequires:  tokyocabinet-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
sed -i -r 's/<a id="id[a-z0-9]\+">/<a id="id">/g' docs/manual.html
%install
%{make_install}
rm %{buildroot}%{_pkgdocdir}/INSTALL.md %{buildroot}%{_pkgdocdir}/LICENSE.md
cat %{SOURCE1} >> %{buildroot}%{_sysconfdir}/neomuttrc
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
