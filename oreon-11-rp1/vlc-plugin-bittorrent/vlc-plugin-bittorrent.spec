%global source0_hash bbecd1e3900112f6df4f54bd04aa0f834de7061ddb9ad4b81d870fb051bc1ccf
%global srcname vlc-bittorrent
Name:           vlc-plugin-bittorrent
Version:        2.16
Release:        1%{?dist}
Summary:        Bittorrent plugin for VLC
License:        GPL-3.0-or-later
URL:            https://github.com/johang/vlc-bittorrent
Source0:        https://github.com/johang/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Requires:       vlc-plugins-base%{?_isa}
Obsoletes:      vlc-bittorrent < 2.14-4
Provides:       vlc-bittorrent = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf-archive
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(libtorrent-rasterbar)
BuildRequires:  pkgconfig(vlc-plugin)
# /oreon:deps
%description
With vlc-bittorrent, you can open a .torrent file or magnet link with
VLC and stream any media that it contains.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1
autoreconf -vif
# do not hardcode vlc path, for flatpak builds
sed -i -e 's|/usr/bin/||' data/%{name}.desktop

%build

%if 0%{?fedora} >= 41 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
CXXFLAGS="$CXXFLAGS -DOPENSSL_NO_ENGINE"
%endif
%configure --disable-static --libdir=%{vlc_plugindir}/access
%make_build
%install
%make_install
find %{buildroot}%{_libdir} -name "*.la" -delete
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
