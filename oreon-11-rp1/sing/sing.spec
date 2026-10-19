%global source0_hash aed0af97180a25926f8a0bf83ddfa301ac7ab6b6c3f01ab111d855b4dafa2b77
Summary:        Sends fully customized ICMP packets from command line
Name:           sing
Version:        1.1
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            https://sourceforge.net/projects/%{name}/
Source0:        https://downloads.sourceforge.net/%{name}/SING-%{version}.tgz
Patch0:         sing-1.1-fedora.patch
Patch1:         sing-1.1-suid_log.patch
Patch2:         sing-1.1-sys_errlist.patch
Patch3:         sing-c99.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libnet10-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
# /oreon:deps
%description
Sing is a little tool that sends fully customized ICMP packets from command
line. The main purpose is to replace/complement the nice ping command with
certain enhancements as:

 - Send fragmented and monster packets > 65534 bytes
 - Send/read spoofed packets
 - Send many ICMP Information types in addition to the echo request type,
   sent by default as address mask request, timestamp, information request,
   router solicitation and router advertisement
 - Send many ICMP error types: redirect, source quench, time exceeded,
   destination unreach and parameter problem
 - Send to host with loose or strict source routing
 - Use little fingerprinting techniques to discover Windows or Solaris boxes
 - Send ICMP packets emulating certain OS: Cisco, Solaris, Linux, Shiva,
   Unix and Windows at the moment

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n SING-%{version} -p1

# Rebuilding of configure file is needed for Patch0
autoconf

# Automake can't be run because of missing Makefile.am
cp -f %{_datadir}/automake-*/config.* .

%build

%configure --bindir=%{_sbindir}
%make_build
%install
%make_install
iconv -f iso-8859-1 -t utf-8 -o LEEME.utf8 LEEME
touch -c -r LEEME LEEME.utf8
mv -f LEEME.utf8 LEEME
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
