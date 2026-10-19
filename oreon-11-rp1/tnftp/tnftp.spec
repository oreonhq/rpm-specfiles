%global source1_hash d42bf296ee436f42b67c1ca044343200d32928150458c353e2decbc4bf09cac5
%global source0_hash 101cda6927e5de4338ad9d4b264304d7d15d6a78b435968a7b95093e0a2efe03
Name:          tnftp
Version:       20260211
Release:        1%{?dist}
Summary:        FTP (File Transfer Protocol) client from NetBSD
License:       0BSD AND BSD-2-Clause AND BSD-3-Clause AND ISC
URL:           http://www.NetBSD.org/
Source0:        http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz
Source1:       http://ftp.netbsd.org/pub/NetBSD/misc/%{name}/%{name}-%{version}.tar.gz.asc
Source2:       gpgkey-2A8E22EDB07B5414548D8507A4186D9A7F332472.gpg
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnupg2
BuildRequires:  libedit-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
