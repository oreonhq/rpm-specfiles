%global source0_hash be0134394bd7d418a3b34892b0709eeb848557e86474e1786f0d1a887d3a6580

Name:          tnftp
Version:       20230507
Release:       7%{?dist}
Summary:       FTP (File Transfer Protocol) client from NetBSD

License:       0BSD AND BSD-2-Clause AND BSD-3-Clause AND ISC

# From the README:
# `tnftp' is a `port' of the NetBSD FTP client to other systems.
# See http://www.NetBSD.org/ for more details about NetBSD.
URL:           http://www.NetBSD.org/
Source0:       http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz
Source1:       http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz.asc
Source2:       gpgkey-2A8E22EDB07B5414548D8507A4186D9A7F332472.gpg

BuildRequires: make
BuildRequires: libedit-devel
BuildRequires: openssl-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gnupg2

%description
%{name} is the FTP (File Transfer Protocol) client from NetBSD.  FTP
is a widely used protocol for transferring files over the Internet and
for archiving files.  %{name} provides some advanced features beyond
the Linux netkit ftp client, but maintains a similar user interface to
the traditional ftp client.  It was formerly called lukemftp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build
export CFLAGS="%{optflags}"
%configure --enable-editcomplete \
           --without-local-libedit \
           --enable-ipv6 \
           --enable-ssl
%make_build

%install
%make_install

%files
%doc ChangeLog INSTALL NEWS README THANKS todo
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
