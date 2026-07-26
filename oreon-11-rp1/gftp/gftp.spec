%global source0_hash fb134d5479a6b81251b9d37be7264fb8be6edb07bce98569e0e0ba9570587fd6

Summary: A multi-threaded FTP client for the X Window System
Name: gftp
Version: 2.9.1b
Release: 12%{?dist}
Epoch: 2
License: GPL-2.0-or-later
Url: https://github.com/masneyb/gftp/tags
Source0: https://github.com/masneyb/gftp/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:  pointer-types.patch
Patch1:  autopoint.patch

BuildRequires: gcc
BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: autoconf automake gettext-devel

%description
gFTP is a multi-threaded FTP client for the X Window System. gFTP
supports simultaneous downloads, resumption of interrupted file
transfers, file transfer queues to allow downloading of multiple
files, support for downloading entire directories/subdirectories,
a bookmarks menu to allow quick connection to FTP sites, caching of
remote directory listings, local and remote chmod, drag and drop, 
a connection manager and much more.

Install gftp if you need a graphical FTP client.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p0
%patch -P 1 -p0

%build
./autogen.sh
%configure

make CFLAGS="$RPM_OPT_FLAGS -std=gnu17"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 

# desktop-file-install is picky about this
#sed -i -e "s#Icon=gftp.png#Icon=/usr/share/pixmaps/gftp.png#" \
#  $RPM_BUILD_ROOT%{_datadir}/applications/gftp.desktop
   
desktop-file-install --vendor net --delete-original         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --remove-category Application                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/gftp.desktop

%find_lang %name

%files -f %{name}.lang
%license LICENSE
%doc ChangeLog README.md TODO AUTHORS LICENSE USERS-GUIDE
%{_bindir}/gftp
%{_bindir}/gftp-gtk
%{_bindir}/gftp-text
%{_datadir}/gftp
%{_datadir}/icons/hicolor/*/apps/gftp.*
%{_datadir}/applications/net-gftp.desktop
%{_mandir}/man1/gftp.1.gz

%changelog
%autochangelog
