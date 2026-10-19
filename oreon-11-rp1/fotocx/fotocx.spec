%global source0_hash cdd1e69ba9cae05fa00c9ce20fb13886dc09242a8896adde658fc32ca67ecbc4
Name:    fotocx
Version: 26.61
Release:        1%{?dist}
Summary:        Photo editor
License: GPL-3.0-or-later
URL:     https://kornelix.net/fotocx/fotocx.html
Source0:        https://kornelix.net/downloads/downloads/fotocx-%{version}-source.tar.gz
Source1: %{name}.desktop
ExcludeArch:    %{ix86}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
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
Provides: fotoxx = %{version}-%{release}
Obsoletes: fotoxx < 23.82-5
# oreon:deps
BuildRequires:  clutter-gtk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  lcms2-devel
BuildRequires:  libappstream-glib
BuildRequires:  libchamplain-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libjxl-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
# /oreon:deps
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
rm -f %{buildroot}%{_bindir}/fotocx-snap
ln -s %{_bindir}/fotocx %{buildroot}%{_bindir}/fotocx-snap
rm -f %{buildroot}%{_prefix}/applications/fotocx.desktop
rm -f %{buildroot}%{_datadir}/icons/fotocx.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
