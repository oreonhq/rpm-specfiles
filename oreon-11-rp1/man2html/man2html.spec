# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ccdcb8c3f4e0080923d7e818f0e4a202db26c46415eaef361387c20995b8959f
%global source1_hash 5da5d293a1fcc8e7e18ca3e423a7d8fd0cb1a68b5120f5746efecd1f9c68161f
%global source2_hash e8b5520fc21781d30b176104b49366d21f07bb93aa9fbdf2907f824fed244c9e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global posttag g
%global debian_release 16

Name:       man2html
Version:    1.6
Release:    42.%{posttag}%{?dist}
Summary:    Convert man pages to HTML - CGI scripts

License:    GPL-2.0-or-later AND GPL-1.0-or-later AND man2html

URL:        http://www.kapiti.co.nz/michael/vhman2html.html
Source0:    http://primates.ximian.com/~flucifredi/man/man-%{version}%{posttag}.tar.gz
Source1:    https://ftp.debian.org/debian/pool/main/m/man2html/man2html_%{version}%{posttag}-%{debian_release}.debian.tar.xz
Source2:    man2html.conf

Patch1001:  001-hman-bashism.patch
Patch1002:  002-man2html-default-cgibase.patch
Patch1004:  004-spelling.patch
Patch1011:  011-man2html-doctype-status.patch
Patch1012:  012-man2html-TH.patch
Patch1013:  013-man2html-file-link.patch
Patch1017:  017-man2html.seealso.patch
Patch1018:  018-man2html-quotes.patch
Patch1019:  019-man2html-noindex-segfault.patch
Patch1020:  020-man2html-escape_N.patch
Patch1022:  022-man2html-it-manpage.patch
Patch1023:  023-man2html-double-quotes.patch
Patch1024:  024-man2html-uncompress.patch
Patch1025:  025-man2html-macro-all-args.patch
Patch1026:  026-man2html-macro-longname.patch
Patch1027:  027-man2html-macro-priority.patch
Patch1028:  028-man2html-segfault.patch
Patch1029:  029-man2html-new-macros.patch
Patch1030:  030-man2html-man-hyphens.patch
Patch1031:  031-man2html-BR-empty-line.patch
Patch1032:  032-man2html-man-remove-LO-tags.patch
Patch1033:  033-gcc-warnings.patch
Patch1034:  034-UTF8-charset.patch
Patch1036:  036-fix-tbl-font-parsing.patch
Patch1037:  037-man2html-Nm-and-Bk-mdoc.patch
Patch1038:  038-man2html-colon-escape-sequence.patch
Patch1042:  042-man2html-CVE-2021-40647.patch
Patch1043:  043-man2html-fix-asan-issues.patch

Patch1:  man2html-paths.patch
Patch4:  man2html-cgi.patch
Patch5:  man2html-hman.patch
Patch6:  man2html-doc.patch
Patch8:  man2html-hman-section.patch
Patch9:  man2html-localized-manpage-paths.patch
Patch10: man2html-suffixes.patch
Patch11: man2html-configure-c99.patch
Patch12: man2html-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
BuildRequires:  recode

Requires:   %{name}-core%{?_isa} = %{version}-%{release}
Requires:   httpd

%description
man2html is a man page to HTML converter.

This package contains CGI scripts that allow you to view, browse, and search
man pages using a web server.

%package core
Summary:  Convert man pages to HTML

%description core
man2html is a man page to HTML converter.

This package contains the man2html executable.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%autosetup -p1 -n man-%{version}%{posttag} -a1

%build
CFLAGS="${CFLAGS:-%optflags} -std=gnu17" ; export CFLAGS ;

./configure -d +fhs
make %{?_smp_mflags}

cd debian/sources
make %{?_smp_mflags}

%install
make -C man2html DESTDIR=%{buildroot} install install-hman

make -C debian/sources DESTDIR=%{buildroot} install

install -Dpm0644 man2html/locales/fr/man2html.1 %{buildroot}%{_mandir}/fr/man1/man2html.1
install -Dpm0644 man2html/locales/it/man2html.1 %{buildroot}%{_mandir}/it/man1/man2html.1
install -Dpm0644 man2html/locales/it/hman.1 %{buildroot}%{_mandir}/it/man1/hman.1

recode latin1..utf8 \
    %{buildroot}%{_mandir}/fr/man1/man2html.1 \
    %{buildroot}%{_mandir}/it/man1/man2html.1 \
    %{buildroot}%{_mandir}/it/man1/hman.1 

install -Dpm0644 %SOURCE2 %{buildroot}%{_sysconfdir}/httpd/conf.d/man2html.conf

mkdir -p %{buildroot}%{_localstatedir}/cache/man2html

%post
rm -f %{_localstatedir}/cache/man2html/* || :

%files
%attr(0755,-,-) %{_bindir}/hman
%{_prefix}/lib/man2html/
%attr(0775,root,apache) %{_localstatedir}/cache/man2html
%config(noreplace) %{_sysconfdir}/httpd/conf.d/man2html.conf
%{_mandir}/man1/hman.1.*

%files core
%{_bindir}/man2html
%{_mandir}/man1/man2html.1.*
%{_mandir}/*/man1/*.1.*
%doc COPYING HISTORY man2html/README man2html/TODO

%changelog
%autochangelog
