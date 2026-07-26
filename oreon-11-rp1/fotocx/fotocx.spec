%global source0_hash cdd1e69ba9cae05fa00c9ce20fb13886dc09242a8896adde658fc32ca67ecbc4

Name:    fotocx
Version: 26.2
Release: 1%{?dist}
Summary: Photo editor

License: GPL-3.0-or-later
URL:     https://kornelix.net/fotocx/fotocx.html
Source0: https://kornelix.net/downloads/downloads/fotocx-%{version}-source.tar.gz
Source1: %{name}.desktop

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

BuildRequires: gcc-c++
BuildRequires: gtk3-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
BuildRequires: libtiff-devel
BuildRequires: lcms2-devel
BuildRequires: libchamplain-devel
BuildRequires: clutter-gtk-devel
BuildRequires: make
BuildRequires: libjxl-devel

# Presence checked at build time
Requires: perl-Image-ExifTool
Requires: xdg-utils
Requires: dcraw
Requires: xmessage
Requires: hicolor-icon-theme

Recommends: binutils
Recommends: ffmpeg-free
Recommends: ImageMagick
Recommends: libheif-tools
Recommends: libwebp-tools
Recommends: openjpeg2-tools
Recommends: rawtherapee
Recommends: vlc-cli vlc-plugins-video-out

# Drop after Fedora 43
Provides: fotoxx = %{version}-%{release}
Obsoletes: fotoxx < 23.82-5

%description
Fotocx is a free open source Linux program for editing image files
from a digital camera. The goal of fotocx is to meet most image editing
needs while remaining easy to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}
# make binutils optional
sed -i -e '/addr2line/s/"yes"/"no"/' fotocx.cc

%build
# This package's Makefile is bizarre
# Misc. environment tweaks to let Makefile honor %%{optflags}
make %{?_smp_mflags} PREFIX=%{_prefix} \
    CXXFLAGS="%{optflags}" \
    LDFLAGS="%{build_ldflags}"

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} DOCDIR=%{_pkgdocdir}
install -Dm 644 -p %{name}.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

desktop-file-install --vendor="" \
    --mode 644 \
    --remove-category="Application" \
    --dir %{buildroot}%{_datadir}/applications/ \
    %{SOURCE1}

sed -i /release/d %{buildroot}%{_metainfodir}/*%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*%{name}.metainfo.xml

#symlink identical binaries
rm -f %{buildroot}%{_bindir}/fotocx-snap
ln -s %{_bindir}/fotocx %{buildroot}%{_bindir}/fotocx-snap

# Drop unused
rm -f %{buildroot}%{_prefix}/applications/fotocx.desktop
rm -f %{buildroot}%{_datadir}/icons/fotocx.png

%files
%license doc/copyright
%doc doc/*
%{_mandir}/man1/%{name}.1*
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_metainfodir}/*%{name}.metainfo.xml

%changelog
%autochangelog
