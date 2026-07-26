%global source0_hash be8b3c04fd8a3ef177790895c1a9d11851b0109f1cf1bbbea80904fe6bb6c996

# https://gcc.gnu.org/gcc-10/porting_to.html#common
# https://github.com/ve7fet/linuxax25/issues/7
%define _legacy_common_support 1

Name:		ax25-tools
Version:	1.0.4
Release:	17%{?dist}
Summary:	Tools used to configure an ax.25 enabled computer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://www.linux-ax25.org/wiki/LinuxAX25

# Official upstream is not active, moving to supported fork.
# https://github.com/ve7fet/linuxax25
Source0:        https://github.com/ve7fet/linuxax25/archive/ax25tools-%{version}.tar.gz
Source1:	smdiag.desktop
Source2:	xfhdlcchpar.desktop
Source3:	xfhdlcsd.desktop
Source4:	xfsmdiag.desktop
Source5:	xfsmmixer.desktop
#Temporary Icon
Source6:	%{name}.png

BuildRequires:	automake gcc gcc-c++
BuildRequires:	libax25-devel
BuildRequires:	ncurses-devel
BuildRequires:	libXt-devel
BuildRequires:	libXi-devel
BuildRequires:	fltk1.3-devel
BuildRequires:	libX11-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:	desktop-file-utils
BuildRequires: make

%description
ax25-tools is a collection of tools that are used to configure an ax.25 enabled
computer. They will configure interfaces and assign callsigns to ports as well
as Net/ROM and ROSE configuration.  This package only contains the command
line programs; the GUI programs are contained in ax25-tools-x package.

 * m6pack - handle multiple 6pack TNCs on a single interface
 * ax25d - general purpose AX.25, NET/ROM and Rose daemon
 * axctl - configure/Kill running AX.25 connections
 * axparms - configure AX.25 interfaces
 * axspawn - allow automatic login to a Linux system
 * beacon - transmit periodic messages on an AX.25 port
 * bpqparms - configure BPQ ethernet devices
 * mheardd - display AX.25 calls recently heard
 * rxecho - transparently route AX.25 packets between ports
 * mheard - collect information about packet activity
 * dmascc_cfg - configure dmascc devices
 * sethdlc - get/set Linux HDLC packet radio modem driver port information
 * smmixer - get/set Linux soundcard packet radio modem driver mixer
 * kissattach - Attach a KISS or 6PACK interface
 * kissnetd - create a virtual network
 * kissparms - configure KISS TNCs
 * mkiss - attach multiple KISS interfaces
 * net2kiss - convert a network AX.25 driver to a KISS stream on a pty
 * netromd - send and receive NET/ROM routing messages
 * nodesave - saves NET/ROM routing information
 * nrattach - start a NET/ROM interface
 * nrparms - configure a NET/ROM interface
 * nrsdrv - KISS to NET/ROM serial converter
 * rsattach - start a ROSE interface
 * rsdwnlnk - user exit from the ROSE network
 * rsmemsiz - monitor the ROSE subsystem
 * rsusers.sh - monitor AX.25, NET/ROM and ROSE users
 * rsparms - configure a ROSE interface
 * rsuplnk - User entry into the ROSE network
 * rip98d - RIP98 routing daemon
 * ttylinkd - TTYlink daemon for AX.25, NET/ROM, ROSE and IP
 * ax25_call - Make an AX.25 connection
 * netrom_call - Make a NET/ROM connection
 * rose_call - Make a ROSE connection
 * tcp_call - Make a TCP connection
 * yamcfg - configure a YAM interface

%package x
Summary:	X tools used to configure an AX.25 enabled computer
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description x
ax25-tools-x is a collection of tools that are used to configure an ax.25 enabled
computer.  This package contains the GUI programs to configure Baycom modem
and sound modem.

 * smdiag - Linux soundcard packet radio modem driver diagnostics utility
 * xfhdlcchpar - kernel HDLC radio modem driver channel parameter utility
 * xfhdlcst - kernel HDLC radio modem driver status display utility
 * xfsmdiag - kernel soundcard radio modem driver diagnostics utility
 * xfsmmixer - kernel soundcard radio modem driver mixer utility

%package docs
Summary:	Documentation for ax25-tools and ax25-tools-x
BuildArch:      noarch

%description docs
ax25-tools is a collection of tools that are used to configure an ax.25 enabled
computer.  This package contains the GUI programs to configure Baycom modem
and sound modem. This package contains the documentation for ax25-tools and
ax25-tools-x

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ax25tools-%{version}

%build
./autogen.sh
%configure --with-xutils
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

# no upstream .desktop or icon yet so we'll use a temporary one
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
cp %{SOURCE6} ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/%{name}.png
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE3}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE4}
desktop-file-install	\
	--dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE5}

#don't include these twice
rm -rf $RPM_BUILD_ROOT%{_docdir}/ax25tools

%files
%doc AUTHORS ChangeLog
%doc doc/README*
%license COPYING
%{_bindir}/*
%{_sbindir}/*
%{_localstatedir}/ax25/mheard/
%config(noreplace) %{_sysconfdir}/ax25/ax25.profile
%config(noreplace) %{_sysconfdir}/ax25/ax25d.conf
%config(noreplace) %{_sysconfdir}/ax25/axports
%config(noreplace) %{_sysconfdir}/ax25/axspawn.conf
%config(noreplace) %{_sysconfdir}/ax25/nrbroadcast
%config(noreplace) %{_sysconfdir}/ax25/nrports
%config(noreplace) %{_sysconfdir}/ax25/rip98d.conf
%config(noreplace) %{_sysconfdir}/ax25/rsports
%config(noreplace) %{_sysconfdir}/ax25/rxecho.conf
%config(noreplace) %{_sysconfdir}/ax25/ttylinkd.conf
%exclude %{_bindir}/smdiag
%exclude %{_sbindir}/xfhdlcchpar
%exclude %{_sbindir}/xfhdlcst
%exclude %{_sbindir}/xfsmdiag
%exclude %{_sbindir}/xfsmmixer

%files x
%{_bindir}/smdiag
%{_sbindir}/xfhdlcchpar
%{_sbindir}/xfhdlcst
%{_sbindir}/xfsmdiag
%{_sbindir}/xfsmmixer
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop

%files docs
%doc COPYING
%{_mandir}/man?/*

%changelog
%autochangelog
