%global source0_hash 91384d133d72671863494dd9742bc622b4089ea8ea760884a5b8c34095d76dc5
Name: tin
Version: 2.6.5
Release:        3%{?dist}
Summary:        Basic Internet news reader
License: BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL: http://www.tin.org/
Source0:        ftp://ftp.tin.org/pub/news/clients/tin/stable/tin-%{version}.tar.xz
# oreon:deps
BuildRequires:  aspell
BuildRequires:  byacc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  libcanlock-devel
BuildRequires:  libgsasl-devel
BuildRequires:  libicu-devel
BuildRequires:  libidn-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-generators
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
