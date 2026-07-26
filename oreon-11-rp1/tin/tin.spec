%global source0_hash 91384d133d72671863494dd9742bc622b4089ea8ea760884a5b8c34095d76dc5

Name: tin
Version: 2.6.5
Release: 3%{?dist}
Summary: Basic Internet news reader
# all sources built into binaries are BSD-3-Clause except
# src/parsdate.{c,y} which are Public Domain
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL: http://www.tin.org/
Source0: ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz
BuildRequires: aspell
BuildRequires: byacc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnupg2
BuildRequires: libcanlock-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: perl-generators
BuildRequires: libgsasl-devel
BuildRequires: libicu-devel
BuildRequires: libidn-devel
BuildRequires: zlib-devel

%description
Tin is a basic, easy to use Internet news reader.  Tin can read news
locally or remotely via an NNTP (Network News Transport Protocol)
server.

Install tin if you need a basic news reader.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -rv libcanlock pcre

%build
%configure \
	--with-libdir=/var/lib/news \
	--with-spooldir=/var/spool/news/articles \
	--enable-cancel-locks \
	--enable-long-article-numbers \
	--enable-nntp \
	--enable-prototypes \
	--disable-echo \
	--disable-mime-strict-charset \
	--with-screen=ncursesw \
	--with-gpg=%{_bindir}/gpg2 \
	--with-mime-default-charset=UTF-8 \
	--with-nntps=openssl \
	--with-pcre2-config=/usr/bin/pcre2-config \
	--with-zlib \

sed -i -e 's/@\$(INSTALL) -s/@\$(INSTALL)/g' -e 's/@\$(CC)/\$(CC)/g' -e  's/@\$(CPP)/\$(CPP)/g' src/Makefile

%make_build

%install
%make_install

install -Dpm644 -t %{buildroot}%{_mandir}/man3 doc/wildmat.3

%find_lang %{name}

%files -f %name.lang
%doc README
%doc doc/{CHANGES{,.old},CREDITS,TODO,WHATSNEW}
%doc doc/{config-anomalies,filtering,good-netkeeping-seal}
%doc doc/*.{sample,txt}
%doc doc/tin.defaults
%{_bindir}/tin
%{_bindir}/rtin
%{_bindir}/metamutt
%{_bindir}/opt-case.pl
%{_bindir}/w2r.pl
%{_bindir}/url_handler.pl
%{_bindir}/tinews.pl
%{_mandir}/man1/opt-case.pl.1*
%{_mandir}/man1/rtin.1*
%{_mandir}/man1/tin.1*
%{_mandir}/man1/tinews.pl.1*
%{_mandir}/man1/url_handler.pl.1*
%{_mandir}/man1/w2r.pl.1.gz
%{_mandir}/man3/wildmat.3*
%{_mandir}/man5/mbox.5*
%{_mandir}/man5/mmdf.5*
%{_mandir}/man5/rtin.5*
%{_mandir}/man5/tin.5*

%changelog
%autochangelog
