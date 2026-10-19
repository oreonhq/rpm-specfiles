%global source0_hash 394a43d205f06d6cf038bb36999793cb39da5568c5f9d8b40915f68776bf64a2
Name:           telepathy-salut
Version:        0.99.11
Release:        1%{?dist}
Summary:        Link-local XMPP telepathy connection manager
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/FrontPage
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         telepathy-salut-0.8.1-python3.patch
Patch1:         telepathy-salut-0.8.1-gcc14-fix-incompatible-pointer-types.patch
Requires:	telepathy-filesystem
# oreon:deps
BuildRequires:  avahi-gobject-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-daemon
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtk-doc
BuildRequires:  libasyncns-devel
BuildRequires:  libsoup-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-dbus
BuildRequires:  sqlite-devel
BuildRequires:  telepathy-glib-devel
# /oreon:deps
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
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*.html
%oreon_autofiles main

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
