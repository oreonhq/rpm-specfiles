%global source0_hash c363f04149f97baf1c5e10ac90677b8309724f2042ab045a45041cfb7b44649b

%global _preprocessor_defines %{_preprocessor_defines} -DOPENSSL_NO_ENGINE

Summary:	FUSE filesystem Bittorrent
Name:		fuse-btfs
Version:	3.1
Release:	%autorelease

License:	GPL-3.0-only
URL:		https://github.com/johang/btfs
Source0:	https://github.com/johang/btfs/archive/v%{version}/btfs-%{version}.tar.gz

# FTBFS with FUSE3
ExcludeArch:	i686

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig(fuse3)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(libcurl)

%description
With BTFS, you can mount any .torrent file or magnet link and then use it as
any read-only directory in your file tree. The contents of the files will be
downloaded on-demand as they are read by applications. Tools like ls, cat and
cp works as expected. Applications like vlc and mplayer can also work without
changes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n btfs-%{version}

%build
autoreconf -i
%configure
%make_build

%install
%{make_install}

%files
%{_bindir}/btfs
%{_bindir}/btfsstat
%{_bindir}/btplay
%{_mandir}/man1/btfs.1*

%doc README.md
%license LICENSE

%changelog
%autochangelog
