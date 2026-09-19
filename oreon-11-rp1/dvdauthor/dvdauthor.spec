%global source0_hash 3020a92de9f78eb36f48b6f22d5a001c47107826634a785a62dfcd080f612eb7

Name:           dvdauthor
Version:        0.7.2
Release:        29%{?dist}
Summary:        Command line DVD authoring tool

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://dvdauthor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
# From openSUSE
Patch0:         dvdauthor-0.7.2-imagemagick7.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libdvdread-devel >= 0.9.4-4
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:  fontconfig-devel
BuildRequires:  fribidi-devel
BuildRequires:  freetype-devel
BuildRequires:  ImageMagick-devel >= 1:7.0

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
DVDAuthor is a set of tools to help you author the file and directory
structure of a DVD-Video disc, including programmatic commands for
implementing interactive behavior. It is driven by command lines and
XML control files, though there are other programs that provide
GUI-based front ends if you prefer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

%build
export LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed,-z noexecstack" # *Magick-config linkage bloat
%configure --disable-rpath --enable-default-video-format=NTSC
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README TODO
%{_bindir}/dvdauthor
%{_bindir}/dvddirdel
%{_bindir}/dvdunauthor
%{_bindir}/mpeg2desc
%{_bindir}/spumux
%{_bindir}/spuunmux
%{_datadir}/dvdauthor/
%{_mandir}/man1/dvdauthor.1*
%{_mandir}/man1/dvddirdel.1*
%{_mandir}/man1/dvdunauthor.1*
%{_mandir}/man1/mpeg2desc.1*
%{_mandir}/man1/spumux.1*
%{_mandir}/man1/spuunmux.1*
%{_mandir}/man7/video_format.7*

%changelog
%autochangelog
