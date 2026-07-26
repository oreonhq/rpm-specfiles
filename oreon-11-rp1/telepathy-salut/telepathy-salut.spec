%global source0_hash 70b9108ac8b511b7688e1b580de4ddb8981603c3cbde01f287ef8f9cb708618e

Name:           telepathy-salut
Version:        0.8.1
Release:        35%{?dist}
Summary:        Link-local XMPP telepathy connection manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
# python3
Patch0:         telepathy-salut-0.8.1-python3.patch
# Fix compilation with gcc14 -Werror=incompatible-pointer-types
Patch1:         telepathy-salut-0.8.1-gcc14-fix-incompatible-pointer-types.patch

BuildRequires: make
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:	dbus-glib-devel >= 0.61
BuildRequires:	python3-dbus
BuildRequires:	avahi-gobject-devel
BuildRequires:	libxml2-devel
# Use gnutls as wocky backend
# wocky defaults to gnutls : see
# https://gitlab.freedesktop.org/telepathy/wocky/-/commit/71d67e44ce3072ebeae477f1b493bbb80f6f7958
# also, due to https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
# code depending on ENGINE API (wocky-openssl.c) no longer compiles
BuildRequires:	gnutls-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	libxslt
BuildRequires:	libasyncns-devel >= 0.3
BuildRequires:	telepathy-glib-devel >= 0.17.1
BuildRequires:  libuuid-devel
BuildRequires:	libsoup-devel
BuildRequires:	sqlite-devel
BuildRequires:  gtk-doc
# for tests
BuildRequires:  dbus-daemon

Requires:	telepathy-filesystem

%description
%{name} is a Telepathy connection manager for link-local XMPP.
Normally, XMPP does not support direct client-to-client interactions,
since it requires authentication with a server.  This package makes
it is possible to establish an XMPP-like communications system on a
local network using zero-configuration networking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .py3
%patch -P1 -p1 -b .pointer_type

%build
export PYTHON=python3
%configure --enable-ssl --enable-olpc --disable-avahi-tests --enable-static=no
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

## Don't package html doc to incorrect doc directory
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*.html

%check
make check

%ldconfig_scriptlets

%files
%doc COPYING AUTHORS NEWS README docs/clique.xml
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/salut-0
%dir %{_libdir}/telepathy/salut-0/lib
%{_libdir}/telepathy/salut-0/lib/libsalut-plugins-*.so
%{_libdir}/telepathy/salut-0/lib/libsalut-plugins.so
%{_libdir}/telepathy/salut-0/lib/libwocky-telepathy-salut-*.so
%{_libdir}/telepathy/salut-0/lib/libwocky.so

%changelog
%autochangelog
