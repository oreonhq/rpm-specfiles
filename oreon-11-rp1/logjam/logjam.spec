%global source0_hash 6735e98daaa0711f4723865866e89847c9ae2bd20853beebccd8d5056df5ee84

%global use_xmms 0
# this thing is oooold and depends on gtk2.
%global optflags %{optflags} -std=gnu17

Name:		logjam
Version:	4.6.2
Release:	39%{?dist}
Epoch:		1
Summary:	GTK2 client for LiveJournal
License:	GPL-2.0-or-later
URL:		http://logjam.danga.com/
Source0:	http://andy-shev.github.com/LogJam/download/%{name}-%{version}.tar.bz2
# Alternately, we sometimes get source from git
# git clone git://github.com/martine/LogJam.git logjam-git
# find logjam-git -depth -name .git -type d -exec rm -rf {} \;
# tar cvfj logjam-git-20090824.tar.bz2 logjam-git/
# Source0:	logjam-git-20090824.tar.bz2
Requires:	curl >= 7.9, gtkspell
%if %{use_xmms}
BuildRequires:	xmms-devel
%endif
BuildRequires:	curl-devel, gtk2-devel, gtkspell-devel
# This is now a GTK3 component and we cannot use that.
# BuildRequires:	gtkhtml3-devel
BuildRequires:	gettext, desktop-file-utils, aspell-devel, librsvg2-devel
BuildRequires:	libsoup-devel, sqlite-devel, gnutls-devel, libgcrypt-devel
BuildRequires:	autoconf, automake, libtool, intltool, popt-devel, m4
BuildRequires:	dbus-devel, dbus-glib-devel, perl(YAML)
# These are long long ghosts
# Obsoletes:	loserjabber, logjam-gnome
Patch1:		logjam-4.4.1-fedora-desktop.patch
Patch2:		logjam-4.6.2-format-security-fix.patch
Patch3:		logjam-4.6.2-gcc10.patch
Patch4:		logjam-c99.patch
Patch5:		logjam-4.6.2-fix-verify-path-call.patch

%description
This is the new GTK2 client for LiveJournal (http://www.livejournal.com).

%if %{use_xmms}
%package xmms
Summary:	LogJam helper binary
Requires:	logjam, xmms
BuildRequires:	xmms-devel
BuildRequires: make

%description xmms
This is a helper binary for LogJam which is used to get the
current music from XMMS.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .desktop
%patch -P2 -p1 -b .format-security
%patch -P3 -p1 -b .gcc10
%patch -P4 -p1
%patch -P5 -p1 -b .fix-verify-path-call

%build
touch NEWS README AUTHORS
%configure --with-sqlite3 \
%if %{use_xmms}
	--with-xmms
%else
	--without-xmms
%endif
make

%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
# Rename locale dir, bugzilla 210206
if [ -d $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 ]; then
	mv $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 $RPM_BUILD_ROOT%{_datadir}/locale/en_US
fi
%find_lang %{name}
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --add-category X-Fedora                               \
  --delete-original					\
  $RPM_BUILD_ROOT/%{_datadir}/applications/logjam.desktop

%files -f %{name}.lang
%doc doc/README doc/TODO
%license COPYING
%{_bindir}/logjam
%{_mandir}/man1/logjam.1.gz
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/logjam*

%if %{use_xmms}
%files xmms
%{_bindir}/logjam-xmms-client
%endif

%changelog
%autochangelog
