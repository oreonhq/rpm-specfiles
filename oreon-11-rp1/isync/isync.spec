%global source0_hash 28cc90288036aa5b6f5307bfc7178a397799003b96f7fd6e4bd2478265bb22fa

Name:           isync
Version:        1.5.1
Release:        3%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://isync.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.asc
# needs manual removal of leftover html elements
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x63bfd037cad71e8dff3aea3ac17714f08d1bdbba#./%{name}.keyring

BuildRequires:  perl
BuildRequires:  libdb-devel
BuildRequires:  openssl-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  automake
BuildRequires:  gnupg2

Requires:       cyrus-sasl

%description
mbsync is a command line application which synchronizes mailboxes. Currently
Maildir and IMAP4 mailboxes are supported. New messages, message deletions
and flag changes can be propagated both ways. mbsync is suitable for use in
IMAP-disconnected mode.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
# Convert to utf-8
for file in ChangeLog; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

%build
%configure
%make_build

%install
%make_install
# Remove copy of documentation files installed by package's buildsystem.
# Preverred over patching Makefile.am an regenerating Makefile.in due
# to robustness.
rm -r %{buildroot}%{_defaultdocdir}

%files
%doc AUTHORS NEWS README TODO ChangeLog src/mbsyncrc.sample
%license COPYING
%{_bindir}/mbsync
%{_bindir}/mdconvert
%{_bindir}/mbsync-get-cert
%{_mandir}/man1/*

%changelog
%autochangelog
