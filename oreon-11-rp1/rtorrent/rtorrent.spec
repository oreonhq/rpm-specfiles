%global source0_hash 248da813b3b6ff89016b5e11c59e6820857f5fb01dd4aad21843e5a461877cff

Name:          rtorrent
# OpenSSL exception, see README
# Automatically converted from old format: GPLv2+ with exceptions - review is highly recommended.
License:       LicenseRef-Callaway-GPLv2+-with-exceptions
Version:       0.16.2
Release:       3%{?dist}
Summary:       BitTorrent client based on libtorrent 
URL:           https://github.com/rakshasa/rtorrent
Source0:       https://github.com/rakshasa/rtorrent/releases/download/v%{version}/rtorrent-%{version}.tar.gz
Source1:       rtorrent.1

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libsigc++20-devel
BuildRequires: libtorrent-devel >= 0.16.2
BuildRequires: ncurses-devel
BuildRequires: pkgconfig
BuildRequires: xmlrpc-c-devel

%description
A BitTorrent client using libtorrent, which on high-bandwidth connections is 
able to seed at 3 times the speed of the official client. Using
ncurses its ideal for use with screen or dtach. It supports 
saving of sessions and allows the user to add and remove torrents and scanning
of directories for torrent files to seed and/or download.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0
for file in AUTHORS README.md doc/rtorrent.rc COPYING
do
    chmod -x "$file"
done

# Avoid an attempt to re-run autoconf.
touch -r aclocal.m4 scripts/common.m4

%build
%configure --with-xmlrpc-tinyxml2 --enable-ipv6
%make_build

%install
%make_install
install -Dpm 0644 %SOURCE1 %{buildroot}/%{_mandir}/man1/rtorrent.1

%files
%doc AUTHORS README.md doc/rtorrent.rc
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/rtorrent.1.gz
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/lua
%{_datadir}/%{name}/lua/%{name}.lua

%changelog
%autochangelog
