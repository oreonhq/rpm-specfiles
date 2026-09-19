%global source0_hash 0256fcb3086382e7c94ad2b87d69684e3dc28fb7493a37fdd0115b1621bdd3f2

# https://src.fedoraproject.org/rpms/redhat-rpm-config/blob/master/f/buildflags.md#legacy-fcommon
%define _legacy_common_support 1

Name:		newsx
Version:	1.6
Release:	48%{?dist}
# public domain:
# dbz/dbz-v3.c
# dbz/dbz-v6.c
# dbz/endian.c
# src/hash.c
# src/mkcrc.c
# src/mkcrc.rc
#
# dbz/md5.{c,h} are RSA Message-Digest licensed - ignoring per https://gitlab.com/fedora/legal/fedora-license-data/-/issues/440
# lib/setenv.c is BSD-4-Clause-UC but not compiled into binary
License:	GPL-2.0-or-later AND Zeeff
Summary:	NNTP news exchange utility
Summary(pl):	Narzędzie do wymiany newsów po NNTP
Source0:	ftp://ftp.tin.org/pub/news/utils/newsx/%{name}-%{version}.tar.gz
# Source0-md5:	ad9c76c53d5c7d21d86bec805fe8cd34
Patch0:		%{name}-make.patch
Patch1:		%{name}-stack.patch
Patch2:		%{name}-quotes.patch
# port to automake 1.12+
Patch3:		%{name}-automake.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:	inn-devel
BuildRequires:	automake
BuildRequires:	autoconf
Requires:	inn

%description
Newsx is an NNTP client that will connect to a remote NNTP server and
post outgoing news articles batched by the news system (e.g. INN), as
well as fetch incoming articles.

%description -l pl
Newsx jest klientem NNTP który łączy się ze zdalnym serwerem i wysyła
wychodzące artykuły zgromadzone przez system newsów (np. INN) oraz
pobiera przychodzące artykuły.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch 0 -p1
%patch 1 -p1 -b .stack
%patch 2 -p1 -b .quotes
%patch 3 -p1 -b .am-1.12

%build
autoreconf -f -i
export CFLAGS="-std=gnu17 %optflags"
%configure \
	--with-inhosts=/var/spool/news/inhosts \
	--with-newsconfig=/usr/lib/news/lib/innshellvars \
	--with-newslib=%{_libdir}/news/lib \

%make_build

%install
%make_install

# avoid conflict with leafnode
pushd $RPM_BUILD_ROOT
mv .%{_bindir}/newsq .%{_bindir}/newsx-newsq
mv .%{_mandir}/man1/newsq.1 .%{_mandir}/man1/newsx-newsq.1
popd

%files
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%license COPYING
%attr(755,root,root) %{_bindir}/*
%attr(770,root,news) %dir /var/spool/news/inhosts
%{_mandir}/man[158]/*

%changelog
%autochangelog
