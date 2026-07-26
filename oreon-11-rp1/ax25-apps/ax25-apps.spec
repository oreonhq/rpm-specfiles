%global source0_hash cd89b99a4637d1ee7829fb137ae5609b7808ad124b313a9afc35312523b905a4

# https://gcc.gnu.org/gcc-10/porting_to.html#common
%define _legacy_common_support 1

Name:		ax25-apps
Version:	2.0.0
Release:	18%{?dist}
Summary:	AX.25 ham radio applications

#ax25ipd is BSD licensed, rest is GPLv2+
# Automatically converted from old format: GPLv2+ and BSD - review is highly recommended.
License:	GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:		https://github.com/ve7fet/linuxax25

# git clone https://github.com/ve7fet/linuxax25.git
# cd linuxax25/ax25apps
# git archive --prefix=ax25apps-2.0.0/ -o ../ax25apps-2.0.0.tar.gz HEAD
Source0:	ax25apps-%{version}.tar.gz

Patch0:     ax25-apps-0.0.6-nongenericnames.patch
Patch1:     ax25-apps-ioctl.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:  make
BuildRequires:	glibc-devel
BuildRequires:	libax25-devel
BuildRequires:	ncurses-devel

%description

This package provides specific user applications for hamradio that use AX.25 
Net/ROM or ROSE network protocols:

 * axcall: a general purpose AX.25, NET/ROM and ROSE connection program.
 * axlisten: a network monitor of all AX.25 traffic heard by the system.
 * ax25ipd: an RFC1226 compliant daemon which provides encapsulation of
   AX.25 traffic over IP.
 * ax25mond: retransmits data received from sockets into an AX.25 monitor
   socket.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ax25apps-%{version}

# termio.h has been obsolete for many years, substitute with termios.h
sed -i "s|termio|termios|" ax25ipd/io.c 
sed -i "s|termio.h||" configure.ac

%build
./autogen.sh
%configure
%make_build

%install
%make_install

#don't include these twice
rm -rf $RPM_BUILD_ROOT%{_docdir}/ax25apps

# Fix the encoding on the doc files to be UTF-8
recode()
{
	iconv -f "$2" -t utf-8 < "$1" > "${1}_"
	mv -f "${1}_" "$1"
}
recode AUTHORS iso-8859-15

%files
%doc AUTHORS ChangeLog README
%doc doc/*
%license COPYING
%config(noreplace) %{_sysconfdir}/ax25/ax25ipd.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25mond.conf
%config(noreplace) %{_sysconfdir}/ax25/ax25rtd.conf
%{_bindir}/*
%{_sbindir}/*
%{_localstatedir}/ax25/ax25rtd/
%{_mandir}/man?/*

%changelog
%autochangelog
