%global source0_hash 6735e98daaa0711f4723865866e89847c9ae2bd20853beebccd8d5056df5ee84
%global use_xmms 0
%global optflags %{optflags} -std=gnu17
Name:		logjam
Version:	4.6.2
Release:        1%{?dist}
Epoch:		1
Summary:        GTK2 client for LiveJournal
License:	GPL-2.0-or-later
URL:		http://logjam.danga.com/
Source0:        http://andy-shev.github.com/LogJam/download/%{name}-%{version}.tar.bz2
Requires:	curl >= 7.9, gtkspell
Patch1:		logjam-4.4.1-fedora-desktop.patch
Patch2:		logjam-4.6.2-format-security-fix.patch
Patch3:		logjam-4.6.2-gcc10.patch
Patch4:		logjam-c99.patch
Patch5:		logjam-4.6.2-fix-verify-path-call.patch
# oreon:deps
BuildRequires:  aspell-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  dbus-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnutls-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsoup-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  perl(YAML)
BuildRequires:  popt-devel
BuildRequires:  sqlite-devel
# /oreon:deps
%description
This is the new GTK2 client for LiveJournal (http://www.livejournal.com).

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
	--without-xmms
make
%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
if [ -d $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 ]; then
	mv $RPM_BUILD_ROOT%{_datadir}/locale/en_US.UTF-8 $RPM_BUILD_ROOT%{_datadir}/locale/en_US
fi
%find_lang %{name}
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
  --add-category X-Fedora                               \
  --delete-original					\
  $RPM_BUILD_ROOT/%{_datadir}/applications/logjam.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
