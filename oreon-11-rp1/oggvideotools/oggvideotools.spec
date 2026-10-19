%global source0_hash 585b8eb913acd503e4bc6d60d4324eec8d0cee2261e94e233e82bff76ab09c10
Name:       oggvideotools
Version:    0.9.1
Release:        1%{?dist}
Summary:        Toolbox for manipulating Ogg video files
License:    GPL-2.0-or-later
URL:        https://dev.streamnik.de/oggvideotools.html
Source0:        https://downloads.sourceforge.net/project/oggvideotools/oggvideotools/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch:      0001-scripts-install-mkSlideshow-as-well.patch
Patch:      0002-scripts-install-to-bin-not-sbin.patch
Patch:      0003-docs-install-to-share-man.patch
Patch:      0004-make-all-internal-libs-STATIC.patch
Patch:      0005-unbundle-libresample.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/mayhem-crash-oggjoin.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/manual-typos.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/oggThumb-zero-getopt-long.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/init-for-valgrind.patch
Patch:      https://sources.debian.org/data/main/o/oggvideotools/0.9.1-3/debian/patches/import-cstring.patch
Patch:      stream-serializer.diff
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  pkgconfig(libresample)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(theoradec)
BuildRequires:  pkgconfig(theoraenc)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
# /oreon:deps
%description
A toolbox for manipulating Ogg video files, which usually consist of a
video stream (Theora) and an audio stream (Vorbis). It includes a
number of handy command line tools for manipulating these video files,
such as for splitting the different streams.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
chmod 644 docs/DocuOggVideoTools.pdf

# Remove bundled libresample
rm -rf src/libresample/

%build

%cmake
%cmake_build
%install
%cmake_install
chmod +x %buildroot%{_bindir}/mkThumbs
chmod +x %buildroot%{_bindir}/mkSlideshow
%global ogg_tool() \
%{_bindir}/ogg%{1}\
%{_mandir}/man1/ogg%{1}.1*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
