%global source2_hash d8a5de668eabd893b6e078072884c8403fb39ac5702ccbcd4372fc008954eb41
%global source1_hash e82ad78cd3f35aed9fed98229a95e9b1e5e8b6bed63c97d730e4adc3a40f8da1
%global source0_hash 28cc90288036aa5b6f5307bfc7178a397799003b96f7fd6e4bd2478265bb22fa
Name:           isync
Version:        1.5.1
Release:        1%{?dist}
Summary:        Tool to synchronize IMAP4 and Maildir mailboxes
License:        GPL-2.0-or-later
URL:            http://isync.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x63bfd037cad71e8dff3aea3ac17714f08d1bdbba#./%{name}.keyring
Requires:       cyrus-sasl
# oreon:deps
BuildRequires:  automake
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gnupg2
BuildRequires:  libdb-devel
BuildRequires:  openssl-devel
BuildRequires:  perl
# /oreon:deps
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
rm -r %{buildroot}%{_defaultdocdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
