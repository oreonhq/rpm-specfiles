%global source0_hash cd89b99a4637d1ee7829fb137ae5609b7808ad124b313a9afc35312523b905a4
%define _legacy_common_support 1
Name:		ax25-apps
Version:	2.0.0
Release:        1%{?dist}
Summary:        AX.25 ham radio applications
License:	GPL-2.0-or-later AND LicenseRef-Callaway-BSD
URL:		https://github.com/ve7fet/linuxax25
Source0:        ax25apps-%{version}.tar.gz
Patch0:     ax25-apps-0.0.6-nongenericnames.patch
Patch1:     ax25-apps-ioctl.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libax25-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
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
rm -rf $RPM_BUILD_ROOT%{_docdir}/ax25apps
recode()
{
	iconv -f "$2" -t utf-8 < "$1" > "${1}_"
	mv -f "${1}_" "$1"
}
recode AUTHORS iso-8859-15
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
