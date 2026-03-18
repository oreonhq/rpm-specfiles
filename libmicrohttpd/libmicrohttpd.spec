Name:           libmicrohttpd
Version:        1.0.2
Release:        3%{?dist}
Epoch:          1
Summary:        Lightweight library for embedding a webserver in applications

# * COPYING says that some main sources are only under LGPL-2.1-or-later
#   and the rest is dual licensed under LGPL-2.1-or-later OR GPL-2.0-or-later WITH eCos-exception-2.0.
# * Some docs are under GFDL-1.3-no-invariants-or-later.
# * Tests and some parts of the build system are under other licenses but they are NOT shipped.
License:        LGPL-2.1-or-later AND (LGPL-2.1-or-later OR GPL-2.0-or-later WITH eCos-exception-2.0) AND GFDL-1.3-no-invariants-or-later

URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://ftp.gnu.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
# Patch0:         gnutls-utilize-system-crypto-policy.patch

BuildRequires:  libtool
BuildRequires:  texinfo
BuildRequires:  gnutls-devel
BuildRequires:  doxygen graphviz
BuildRequires:  make
Requires(post): info
Requires(preun): info

%description
GNU libmicrohttpd is a small C library that is supposed to make it
easy to run an HTTP server as part of another application.
Key features that distinguish libmicrohttpd from other projects are:

* C library: fast and small
* API is simple, expressive and fully reentrant
* Implementation is http 1.1 compliant
* HTTP server can listen on multiple ports
* Support for IPv6
* Support for incremental processing of POST data
* Creates binary of only 25k (for now)
* Three different threading models

%package devel
Summary:        Development files for libmicrohttpd
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for libmicrohttpd

%package doc
Summary:        Documentation for libmicrohttpd
Requires:       %{name} = %{epoch}:%{version}-%{release}
BuildArch:      noarch

%description doc
Doxygen documentation for libmicrohttpd and some example source code

%prep
%autosetup -p1

%build
%configure --disable-static --with-gnutls --enable-https=yes
%make_build
make -C doc/doxygen full

%check
%make_build check

%install
%make_install

rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_bindir}/demo

# Install some examples in /usr/share/doc/libmicrohttpd-doc/examples
mkdir examples
install -m 644 src/examples/*.c examples
install -m 644 doc/examples/*.c examples

cp -R doc/doxygen/html html

%post doc
/sbin/install-info %{_infodir}/libmicrohttpd.info.gz %{_infodir}/dir || :
/sbin/install-info %{_infodir}/libmicrohttpd-tutorial.info.gz %{_infodir}/dir || :

%preun doc
if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/libmicrohttpd.info.gz %{_infodir}/dir || :
/sbin/install-info --delete %{_infodir}/libmicrohttpd-tutorial.info.gz %{_infodir}/dir || :
fi

%files
%doc README NEWS
%license COPYING
%{_libdir}/libmicrohttpd.so.*

%files devel
%{_includedir}/microhttpd.h
%{_libdir}/libmicrohttpd.so
%{_libdir}/pkgconfig/libmicrohttpd.pc

%files doc
%{_mandir}/man3/libmicrohttpd.3.gz
%{_infodir}/libmicrohttpd.info.*
%{_infodir}/libmicrohttpd-tutorial.info.*
%{_infodir}/libmicrohttpd_performance_data.png.gz
%doc AUTHORS README ChangeLog
%doc examples
%doc html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-3
- Prepare for Oreon 11 (RP1)
