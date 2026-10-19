%global source0_hash 32b46ab09759192b4c49f88a640d597aafe6696fc6e3478aec4aefe88ecc022a
%undefine _hardened_build
Summary:        powerful, easy to use console email client
Name: alpine
Version: 2.26
Release:        1%{?dist}
License: Apache-2.0
URL:     https://alpineapp.email/
Source0:        alpine-2.26_patched.tar.xz
Source1: README.fedora
Patch1: alpine-2.24-useragent.patch
Patch2: alpine-2.23-gcc10.patch
Patch3: alpine-configure-c99.patch
Conflicts: pine
Provides: re-alpine = %{version}-%{release}
Requires: hunspell
Requires: mailcap
Requires: /usr/sbin/sendmail
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  hunspell
BuildRequires:  krb5-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  passwd
# /oreon:deps
%description
Alpine -- an Alternatively Licensed Program for Internet
News & Email -- is a tool for reading, sending, and managing
electronic messages.  Alpine is the successor to Pine and was
developed by Computing & Communications at the University of
Washington.  
  Though originally designed for inexperienced email users,
Alpine supports many advanced features, and an ever-growing number of
configuration and personal-preference options.
Changes and enhancements over pine:
  * Released under the Apache Software License, Version 2.0.
  * Internationalization built around new internal Unicode support.
  * Ground-up reorganization of source code around new "pith/" core 
routine library.
  * Ground-up reorganization of build and install procedure based on 
GNU Build System's autotools.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n alpine-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

install -m644 -p %{SOURCE1} .

%build

touch imap/ip6
CFLAGS="%{optflags} -std=gnu17"
%configure \
  --enable-debug=no \
  --without-tcl \
  --with-c-client-target=lfd \
  --with-date-stamp="$(date --utc ${SOURCE_DATE_EPOCH:+--date=@${SOURCE_DATE_EPOCH}})" \
  --with-smtp-msa=/usr/sbin/sendmail \
  --with-npa=/usr/bin/inews \
  --with-passfile=.alpine.passfile \
  --with-simple-spellcheck=hunspell \
  --with-interactive-spellcheck=hunspell \
  --with-system-pinerc=%{_sysconfdir}/pine.conf \
  --with-system-fixed-pinerc=%{_sysconfdir}/pine.conf.fixed
export RPM_BUILD_NCPUS=1
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/pine.conf.fixed
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
