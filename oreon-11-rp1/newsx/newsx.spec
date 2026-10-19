%global source0_hash 0256fcb3086382e7c94ad2b87d69684e3dc28fb7493a37fdd0115b1621bdd3f2
%define _legacy_common_support 1
Name:		newsx
Version:	1.6
Release:        1%{?dist}
License:	GPL-2.0-or-later AND Zeeff
Summary:        NNTP news exchange utility
Summary(pl):	Narzędzie do wymiany newsów po NNTP
Source0:        ftp://ftp.tin.org/pub/news/utils/newsx/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
Patch1:		%{name}-stack.patch
Patch2:		%{name}-quotes.patch
Patch3:		%{name}-automake.patch
Requires:	inn
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  inn-devel
BuildRequires:  make
# /oreon:deps
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
pushd $RPM_BUILD_ROOT
mv .%{_bindir}/newsq .%{_bindir}/newsx-newsq
mv .%{_mandir}/man1/newsq.1 .%{_mandir}/man1/newsx-newsq.1
popd
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
