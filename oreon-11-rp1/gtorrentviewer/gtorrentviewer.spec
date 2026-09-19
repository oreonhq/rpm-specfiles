%global source0_hash 6e56351103f5d46a45be160baa1b7b956b4416fcdb4533b3d17a309665690c95

Name:		gtorrentviewer
Version:	0.2b
Release:	58%{?dist}
Summary:	A GTK2-based viewer and editor for BitTorrent meta files
License:	GPL-1.0-or-later
URL:		http://gtorrentviewer.sourceforge.net/
Source0:	http://downloads.sf.net/gtorrentviewer/GTorrentViewer-%{version}.tar.gz
Patch0:		gtorrentviewer-0.2b-desktop.patch
Patch1:		gtorrentviewer-0.2b-dso-linking.patch
Patch2:		GTorrentViewer-0.2b-tracker-details-refresh.patch
Patch3:		gtorrentviewer-0.2b-trackerdetails.patch
Patch4:		GTorrentViewer-0.2b-curl-types.patch
Patch5:		GTorrentViewer-0.2b-format.patch
Patch6:		GTorrentViewer-0.2b-missing-tracker.patch
Patch7:		gtorrentviewer-configure-c99.patch
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	gtk2-devel >= 2.4
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libcurl-devel

# Scriptlets replaced by File Triggers from Fedora 26 onwards
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
Requires(post):	  desktop-file-utils
Requires(postun): desktop-file-utils
%endif

%description
GTorrentViewer gives you the ability to see and modify all the possible
information from .torrent files without having to start downloading, and
the ability to see in real time the current number of seeds and peers on
the torrent, so you will always know the status before starting the
download.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n GTorrentViewer-%{version}

# Let drag and drop work with URIs as well as files (#206262)
# Also drop ".png" suffix from icon filename, as per Icon Theme spec
%patch -P0

# mainwindow.c requires ceil() from libm (#564928)
%patch -P1 -p1

# Fix crash due to use of uninitialized GValue (#542502, #572806)
%patch -P2 -p1

# Improve tracker support (#674726)
%patch -P3 -p1

# <curl/types.h> went away in curl 7.22.0
%patch -P4 -p1

# Add missing format strings in g_warning() invocations
%patch -P5

# Avoid segfault when dealing with torrent that has no tracker (#1178062)
%patch -P6

# C99 compatibility issues
%patch -P7 -p1

%build
# This package includes its own implementation of SHA1, but with LTO
# on it wants to use openssl's version instead, which we don't link against
# and isn't the same as the local version
%define _lto_cflags %{nil}

%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_datadir}/GTorrentViewer/README
desktop-file-install \
	--vendor "" \
	--add-category X-Fedora \
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/gtorrentviewer.desktop

# Scriptlets replaced by File Triggers from Fedora 26 onwards
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/gtorrentviewer
%{_datadir}/GTorrentViewer
%{_datadir}/applications/gtorrentviewer.desktop
%{_datadir}/pixmaps/gtorrentviewer.png
%{_datadir}/pixmaps/gtorrentviewer.xpm
%{_mandir}/man1/gtorrentviewer.1*

%changelog
%autochangelog
