%global source0_hash 04bfe8ef75db7d629a33de767599765cecadc56274a39822d5d081030d577685
Name:           libmicrohttpd
Version:        1.0.10
Release:        1%{?dist}
Epoch:          1
Summary:        Lightweight library for embedding a webserver in applications
License:        LGPL-2.1-or-later AND (LGPL-2.1-or-later OR GPL-2.0-or-later WITH eCos-exception-2.0) AND GFDL-1.3-no-invariants-or-later
URL:            http://www.gnu.org/software/libmicrohttpd/
Source0:        https://mirrors.kernel.org/gnu/libmicrohttpd/%{name}-%{version}.tar.gz
Requires(post): info
Requires(preun): info
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gnutls-devel
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  texinfo
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
mkdir examples
install -m 644 src/examples/*.c examples
install -m 644 doc/examples/*.c examples
cp -R doc/doxygen/html html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%post doc

/sbin/install-info %{_infodir}/libmicrohttpd.info.gz %{_infodir}/dir || :
/sbin/install-info %{_infodir}/libmicrohttpd-tutorial.info.gz %{_infodir}/dir || :
%preun doc

if [ $1 = 0 ] ; then
/sbin/install-info --delete %{_infodir}/libmicrohttpd.info.gz %{_infodir}/dir || :
/sbin/install-info --delete %{_infodir}/libmicrohttpd-tutorial.info.gz %{_infodir}/dir || :
fi
%files -f %{oreon_filedir}/main.list
%files -n libmicrohttpd-devel -f %{oreon_filedir}/libmicrohttpd-devel.list
%files -n libmicrohttpd-doc -f %{oreon_filedir}/libmicrohttpd-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.2-3
- Prepare for Oreon 11 (RP1)
