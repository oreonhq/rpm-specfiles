%global source0_hash 1cc0414cf524e14bdfacab4ab1cdefd596a2023ea133e224f9d54566ef8b2a75
Name:           sfnt2woff-zopfli
Version:        1.3.1
Release:        1%{?dist}
Summary:        Create WOFF files with Zopfli compression
License:        MPL-1.0 OR GPL-2.0-or-later OR LGPL-2.0-or-later
SourceLicense:  (%{license}) AND Apache-2.0
URL:            https://github.com/bramstein/sfnt2woff-zopfli
Source0:        https://github.com/bramstein/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/pull/18.patch
Patch:          %{url}/pull/20.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(zlib)
BuildRequires:  zopfli-devel
# /oreon:deps
%description
This is a modified version of the sfnt2woff utility that uses Zopfli as a
compression algorithm instead of zlib. This results in compression gains of —
on average — 5-8% compared to regular WOFF files. Zopfli generates compressed
output that is compatible with regular zlib compression so the resulting WOFF
files can be used everywhere.

A corresponding version of the woff2sfnt utility is also provided.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Strip out bundled Zopfli sources
rm -rvf zopfli

%build

%make_build \
    ZLIB_CFLAGS="$(pkg-config --cflags zlib)" \
    ZLIB_LIBS="$(pkg-config --libs zlib)" \
    ZOPFLI_CFLAGS='' \
    ZOPFLI_LIBS='-lzopfli'
%install
install -d '%{buildroot}%{_bindir}'
install -t '%{buildroot}%{_bindir}' -p sfnt2woff-zopfli woff2sfnt-zopfli
install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 \
    sfnt2woff-zopfli.1 woff2sfnt-zopfli.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
