%global source0_hash 766e48423e79359ea31e41db9e5c289675947a7fcf2efdcedb726ac9d0da3784

Summary: A utility for retrieving files using the HTTP or FTP protocols
Name: wget1
Version: 1.25.0
Release: 2%{?dist}
# Generally wget is distributed under GPLv3 or later but there are files in lib/ directory
# which are under LGPLv2.1 or later and are actually built into the resulting rpm.
# This version of wget is built with gnutls so I believe that the 'with openssl'
# part in some files is not applicable here.
License: GPL-3.0-or-later AND LGPL-2.1-or-later
Url: http://www.gnu.org/software/wget/
Source: https://ftp.gnu.org/gnu/wget/wget-%{version}.tar.gz

Patch1: wget-1.17-path.patch

Provides: bundled(gnulib) 
# needed for test suite
BuildRequires: make
BuildRequires: perl(lib)
BuildRequires: perl(English)
BuildRequires: perl(HTTP::Daemon)
BuildRequires: python3
BuildRequires: gnutls-devel
BuildRequires: pkgconfig
BuildRequires: texinfo
BuildRequires: gettext
BuildRequires: autoconf
BuildRequires: libidn2-devel
BuildRequires: libuuid-devel
BuildRequires: perl-podlators
BuildRequires: libpsl-devel
BuildRequires: gpgme-devel
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: git-core

%description
GNU Wget is a file retrieval utility which can use either the HTTP or
FTP protocols. Wget features include the ability to work in the
background while you are logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

%package wget
Summary: %{name} shim to provide wget
Requires: wget1%{?_isa} = %{version}-%{release}
# Replace wget2
Conflicts: wget >= 2.0
Provides: wget = %{version}-%{release}
Provides: wget%{?_isa} = %{version}-%{release}
# From original wget package
Provides: webclient

%description wget
This package provides the shim links for %{name} to be automatically
used in place of wget. This ensures that %{name} is used as
the system provider of wget.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n wget-%{version}

# modify the package string
sed -i "s|\(PACKAGE_STRING='wget .*\)'|\1 (Red Hat modified)'|" configure
grep "PACKAGE_STRING='wget .* (Red Hat modified)'" configure || exit 1

%build
%configure \
    --with-ssl=gnutls \
    --with-libpsl \
    --enable-largefile \
    --enable-opie \
    --enable-digest \
    --enable-ntlm \
    --enable-nls \
    --enable-ipv6 \
    --disable-rpath \
    --without-metalink \
    --disable-year2038

%{make_build}

%install
%{make_install} CFLAGS="%{build_cflags}"
rm -f %{buildroot}%{_infodir}/dir

# Rename the binary and docs
mv %{buildroot}%{_bindir}/wget %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/wget.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Create links for the wget1-wget
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/wget
# Link wget(1) to wget1(1)
echo ".so man1/%{name}.1" > %{buildroot}%{_mandir}/man1/wget.1

%find_lang wget
%find_lang wget-gnulib

##%check
##make check

%files -f wget.lang -f wget-gnulib.lang
%license AUTHORS COPYING
%doc MAILING-LIST NEWS README doc/sample.wgetrc
%{_mandir}/man1/%{name}.*
%{_bindir}/%{name}
%{_infodir}/wget.info.*

%files wget
%{_mandir}/man1/wget.*
%{_bindir}/wget
%config(noreplace) %{_sysconfdir}/wgetrc

%changelog
%autochangelog
