%global source0_hash 766e48423e79359ea31e41db9e5c289675947a7fcf2efdcedb726ac9d0da3784
Summary:        A utility for retrieving files using the HTTP or FTP protocols
Name: wget1
Version: 1.25.0
Release:        2%{?dist}
License: GPL-3.0-or-later AND LGPL-2.1-or-later
Url: http://www.gnu.org/software/wget/
Source0:        https://ftp.gnu.org/gnu/wget/wget-%{version}.tar.gz
Patch1: wget-1.17-path.patch
Provides: bundled(gnulib) 
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  gnutls-devel
BuildRequires:  gpgme-devel
BuildRequires:  libidn2-devel
BuildRequires:  libpsl-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  perl(English)
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(lib)
BuildRequires:  perl-podlators
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  texinfo
BuildRequires:  zlib-devel
# /oreon:deps
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
Conflicts: wget >= 2.0
Provides: wget = %{version}-%{release}
Provides: wget%{?_isa} = %{version}-%{release}
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
mv %{buildroot}%{_bindir}/wget %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/wget.1 %{buildroot}%{_mandir}/man1/%{name}.1
ln -sr %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/wget
echo ".so man1/%{name}.1" > %{buildroot}%{_mandir}/man1/wget.1
%find_lang wget
%find_lang wget-gnulib
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n wget1-wget -f %{oreon_filedir}/wget1-wget.list

%changelog

%autochangelog
