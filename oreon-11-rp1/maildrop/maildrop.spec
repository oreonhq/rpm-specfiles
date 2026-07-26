%global source0_hash b6000075de1d4ffd0d1e7dc3127bc06c04bf1244b00bae853638150823094fec

%global _hardened_build 1

Summary: Mail delivery agent with filtering abilities
Name: maildrop
Version: 3.1.0
Release: 8%{?dist}
# Exception is explicit permission to link to OpenSSL
License: GPL-3.0-only WITH Classpath-exception-2.0
URL: http://www.courier-mta.org/maildrop/
Source0: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2: pubkey.maildrop

BuildRequires: automake, libtool, autoconf
BuildRequires: gcc-c++, gdbm-devel, libdb-devel, pcre2-devel
BuildRequires: gawk
BuildRequires: gnupg
BuildRequires: courier-unicode-devel >= 2.1
BuildRequires: libidn2-devel
BuildRequires: make
#Once this is available uncomment and rebuild
#BuildRequires: courier-authlib-devel

%description
maildrop is the mail filter/mail delivery agent that's used by the
Courier Mail Server. This is a standalone build of the maildrop mail
filter that can be used with other mail servers.

maildrop is a replacement for your local mail delivery agent. maildrop
reads a mail message from standard input, then delivers the message to
your mailbox. maildrop knows how to deliver mail to mbox-style
mailboxes, and maildirs.

maildrop optionally reads instructions from a file, which describe how
to filter incoming mail. These instructions can direct maildrop to
deliver the message to an alternate mailbox, or forward it somewhere
else. Unlike procmail, maildrop uses a structured filtering language.

maildrop is written in C++, and is significantly larger than
procmail. However, it uses resources much more efficiently. Unlike
procmail, maildrop will not read a 10 megabyte mail message into
memory. Large messages are saved in a temporary file, and are filtered
from the temporary file. If the standard input to maildrop is a file,
and not a pipe, a temporary file will not be necessary.

maildrop checks the mail delivery instruction syntax from the filter
file, before attempting to deliver a message. Unlike procmail, if the
filter file contains syntax errors, maildrop terminates without
delivering the message. The user can fix the typo without causing any
mail to be lost.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --disable-shared \
  --enable-use-flock=1 --with-locking-method=fcntl \
  --enable-use-dotlock=1 \
  --enable-syslog=1 \
  --enable-sendmail=%{_sbindir}/sendmail
# prevent 'install: will not overwrite just-created' error
# notification sent to courier-maildrop@lists.sourceforge.net on 2009/09/04
#sed -i 's|DELIVERQUOTAMAN = maildirquota.7 deliverquota.8|DELIVERQUOTAMAN =|' Makefile
%make_build

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot} htmldir=%{_defaultdocdir}/%{name}
cp -pr COPYING COPYING.GPL AUTHORS %{buildroot}%{_defaultdocdir}/%{name}
cp -pr README README.postfix ChangeLog UPGRADE %{buildroot}%{_defaultdocdir}/%{name}

%files
%doc %{_defaultdocdir}/%{name}
%attr(555,root,mail) %{_bindir}/maildrop
%attr(555,root,mail) %{_bindir}/lockmail
%{_bindir}/deliverquota
%{_bindir}/mailbot
%{_bindir}/maildirmake
%{_bindir}/makemime
%{_bindir}/reformail
%{_bindir}/reformime
%{_bindir}/makedat
%{_bindir}/makedatprog
%{_bindir}/maildirwatch
%{_bindir}/maildirkw
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man7/*.7*
%{_mandir}/man8/*.8*

%changelog
%autochangelog
