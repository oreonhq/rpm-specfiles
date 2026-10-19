%global source0_hash 115c91572c72d4a40f0b25b606167b4f2f09441dc7bf1036ccbb1450f1a4969c
%global run_tests 0
Name:           telepathy-gabble
Version:        0.18.4
Release:        27%{?dist}
Summary:        A Jabber/XMPP connection manager
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch1:         telepathy-gabble-0.18.0-build.patch
Patch2:         0001-xmpp-console-Explicitly-state-python-in-the-shebang.patch
Patch3:         telepathy-gabble-0.18.4-python3.patch
Patch4:         telepathy-gabble-0.18.4-xmlerror-constness.patch
Patch5:         telepathy-gabble-0.18.4-aviod-errno-name-confusion.patch
Patch6:         telepathy-gabble-0.18.4-libsoup-3.0.patch
Requires:       telepathy-mission-control >= 5.5.0
Requires:       telepathy-filesystem
Obsoletes:      telepathy-butterfly < 0.5.15-5
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  libnice-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  sqlite-devel
BuildRequires:  telepathy-glib-devel
# /oreon:deps
%description
A Jabber/XMPP connection manager, that handles single and multi-user
chats and voice calls.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p 1 -b .build
%patch -P2 -p 1 -b .shebang
%patch -P3 -p1 -b .py3
%patch -P4 -p1 -b .xmlerror
%patch -P5 -p1 -b .errno
%patch -P6 -p1 -b .soup

autoconf
( cd lib/ext/wocky/ ; autoconf )

%build

%configure --enable-static=no
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*.html
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
