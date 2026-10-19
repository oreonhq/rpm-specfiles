%global source0_hash 3020a92de9f78eb36f48b6f22d5a001c47107826634a785a62dfcd080f612eb7
Name:           dvdauthor
Version:        0.7.2
Release:        1%{?dist}
Summary:        Command line DVD authoring tool
License:        GPL-2.0-or-later
URL:            http://dvdauthor.sourceforge.net/
Source0:        http://downloads.sourceforge.net/dvdauthor/%{name}-%{version}.tar.gz
Patch0:         dvdauthor-0.7.2-imagemagick7.patch
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  ImageMagick-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  libdvdread-devel
BuildRequires:  libpng-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%description
DVDAuthor is a set of tools to help you author the file and directory
structure of a DVD-Video disc, including programmatic commands for
implementing interactive behavior. It is driven by command lines and
XML control files, though there are other programs that provide
GUI-based front ends if you prefer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

export LDFLAGS="$RPM_LD_FLAGS -Wl,--as-needed,-z noexecstack" # *Magick-config linkage bloat
%configure --disable-rpath --enable-default-video-format=NTSC
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
