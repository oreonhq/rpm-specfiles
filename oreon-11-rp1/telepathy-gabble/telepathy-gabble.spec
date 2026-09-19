%global source0_hash 115c91572c72d4a40f0b25b606167b4f2f09441dc7bf1036ccbb1450f1a4969c

%global run_tests 0

Name:           telepathy-gabble
Version:        0.18.4
Release:        27%{?dist}
Summary:        A Jabber/XMPP connection manager

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch1:         telepathy-gabble-0.18.0-build.patch
Patch2:         0001-xmpp-console-Explicitly-state-python-in-the-shebang.patch
# python3
Patch3:         telepathy-gabble-0.18.4-python3.patch
Patch4:         telepathy-gabble-0.18.4-xmlerror-constness.patch
Patch5:         telepathy-gabble-0.18.4-aviod-errno-name-confusion.patch
Patch6:         telepathy-gabble-0.18.4-libsoup-3.0.patch

BuildRequires: make
BuildRequires:  dbus-devel >= 1.1.0
BuildRequires:  dbus-glib-devel >= 0.82
BuildRequires:  telepathy-glib-devel >= 0.19.9
BuildRequires:  glib2-devel >= 2.32
BuildRequires:  gnutls-devel >= 2.12.0
BuildRequires:  sqlite-devel
BuildRequires:  libuuid-devel
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  libnice-devel >= 0.0.11
BuildRequires:  cyrus-sasl-devel
BuildRequires:  libxslt
%if %{run_tests}
# Build Requires needed for tests.
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject
%endif
BuildRequires:  autoconf

Requires:       telepathy-mission-control >= 5.5.0
Requires:       telepathy-filesystem

# Removed in F17
Obsoletes:      telepathy-butterfly < 0.5.15-5

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

%if %{run_tests}
%check
make check
%endif

%build
%configure --enable-static=no
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

## Don't package html doc to incorrect doc directory
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/*.html

%ldconfig_scriptlets

%files
%doc COPYING AUTHORS
%doc docs/*.html
%{_bindir}/%{name}-xmpp-console
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz
## If more connection managers make use of libdir/telepathy this
## be moved to the tp-filesystem spec file.
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/gabble-0
%dir %{_libdir}/telepathy/gabble-0/lib
%dir %{_libdir}/telepathy/gabble-0/plugins
%{_libdir}/telepathy/gabble-0/lib/libgabble-plugins-*.so
%{_libdir}/telepathy/gabble-0/lib/libgabble-plugins.so
%{_libdir}/telepathy/gabble-0/lib/libwocky-telepathy-gabble-*.so
%{_libdir}/telepathy/gabble-0/lib/libwocky.so
%{_libdir}/telepathy/gabble-0/plugins/libconsole.so
%{_libdir}/telepathy/gabble-0/plugins/libgateways.so

%changelog
%autochangelog
