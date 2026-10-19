%global source0_hash 9658625244a88e836bfbed53928c104907fc46bdfffb91225284ea8b6947f5a6
%global _preprocessor_defines %{_preprocessor_defines} -DOPENSSL_NO_ENGINE
Summary:        FUSE filesystem Bittorrent
Name:		fuse-btfs
Version:	3.3
Release:        1%{?dist}
License:	GPL-3.0-only
URL:		https://github.com/johang/btfs
Source0:        https://github.com/johang/btfs/archive/v%{version}/btfs-%{version}.tar.gz
ExcludeArch:	i686
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libtorrent-rasterbar)
# /oreon:deps
%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp works as expected. Applications like vlc and mplayer can also work without
changes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir btfs-%{version}
%oreon_prep
%build

autoreconf -i
%configure
%make_build
%install
%{make_install}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
