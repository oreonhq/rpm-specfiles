%global source0_hash ea63a2aee9f6505b6296a51f4d1f907beb0ecb4bd1e2dd63962b3aed8400f83f

%define _hardened_build 1
Name:           tcputils
Version:        0.6.2
Release:        36%{?dist}
Summary:        Utilities for TCP programming in shell-scripts

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            ftp://ftp.lysator.liu.se/pub/unix/tcputils
Source0:        ftp://ftp.lysator.liu.se/pub/unix/%{name}/%{name}-%{version}.tar.gz
Patch0:         tcputils-0.6.2-makefile.patch

#BuildRequires:  
#Requires:       

BuildRequires: make
BuildRequires:  gcc
%description
This is a collection of programs to facilitate TCP programming in 
shell-scripts. There is also a small library which makes it somewhat 
easier to create TCP/IP sockets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .orig

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
chmod 0644 $RPM_BUILD_ROOT%{_mandir}/man1/*

%files
%doc README
%{_bindir}/getpeername
%{_bindir}/mini-inetd
%{_bindir}/tcpbug
%{_bindir}/tcpconnect
%{_bindir}/tcplisten
%{_mandir}/man1/getpeername.1.gz
%{_mandir}/man1/mini-inetd.1.gz
%{_mandir}/man1/tcpbug.1.gz
%{_mandir}/man1/tcpconnect.1.gz
%{_mandir}/man1/tcplisten.1.gz

%changelog
%autochangelog
