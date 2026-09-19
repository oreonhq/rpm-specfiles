%global source0_hash c6faa022cd8c002165875d4aac83b7a2b59194f0491802924117fc6ac980c778

Summary:	SIP swiss army knife
Name:		sipsak
Version:	0.9.8.1
Release:	%autorelease
License:	GPL-2.0-or-later
URL:		https://github.com/nils-ohlmeier/sipsak
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	gcc
#BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	openssl-devel

%description
sipsak is a small command line tool for developers and
administrators of Session Initiation Protocol (SIP) applications.
It can be used for some simple tests on SIP applications and
devices.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
autoreconf -ivf
%configure --disable-gnutls
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
%autochangelog
