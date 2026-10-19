%global source0_hash eab60847aac34c8768765cecc7821faf50de2636187b452b9b5fa50a12b00bc3
Name:            unifont
Version:         18.0.01
Release:        1%{?dist}
License:         GPL-2.0-or-later AND OFL-1.1 AND GFDL-1.3-or-later
Url:             https://savannah.gnu.org/projects/unifont
Summary:        Tools and glyph descriptions in a very simple text format
Source0:        https://ftp.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:         unifont.metainfo.xml
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  bdf2psf
BuildRequires:  bdftopcf
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-GD
BuildRequires:  perl-generators
BuildRequires:  texinfo
# /oreon:deps
%description
A font with a glyph for every visible Unicode Basic Multilingual Plane code
point and more, with supporting utilities to modify the font. This package
contains tools and glyph descriptions.

%package fonts
BuildArch: noarch
Summary: Unicode font with a glyph for every visible BMP code point
Requires:        fontpackages-filesystem
%description fonts
A fixed-width Unicode font with a glyph for every visible Unicode 7.0 Basic
Multilingual Plane code point (over 55,000 glyphs) and some glyphs beyond BMP.

This font strives for very wide coverage rather than beauty, so use it only as
fallback or for special purposes.

This package contains unicode fonts in OTF format.

%package ttf-fonts
BuildArch: noarch
Summary: Unicode font with a glyph for every visible BMP code point
Requires: (unifont-fonts = %{version}-%{release} if unifont-fonts)
%description ttf-fonts
This package contains unicode fonts in TTF format.
It is provided for compatibility, and unifont-fonts should be used instead.

%package viewer
BuildArch: noarch
Summary: Graphical viewer for unifont
%description viewer
A graphical viewer for unifont source character definitions.

%prep

%setup -q -n unifont-%{version}
# Disable rebuilding during installation
sed -i 's/^install: .*/install:/' Makefile
sed -i 's/install -s/install/' src/Makefile

%build

%make_build CFLAGS='%{optflags}'
make -C font all ttf upperttf
make -C doc unifont.info
%install
%make_install USRDIR=/usr COMPRESS=0 \
  OTFDEST='$(DESTDIR)/usr/share/fonts/unifont'
install -Dm0644 font/compiled/unifont-%{version}.ttf %{buildroot}%{_fontdir}/unifont.ttf
install -Dm0644 font/compiled/unifont_upper-%{version}.ttf %{buildroot}%{_fontdir}/unifont_upper.ttf
find %{buildroot}/usr/share/unifont/ -type f \! -name %{name}.hex -delete
rm -rv %{buildroot}/usr/share/fonts/X11
rm -v %{buildroot}%{_fontdir}/*sample*
install -Dm0644 doc/unifont.info %{buildroot}%{_infodir}/unifont.info
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/unifont.metainfo.xml
rm %{buildroot}/usr/share/consolefonts/Unifont-APL8x16.psf.gz
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n unifont-fonts -f %{oreon_filedir}/unifont-fonts.list
%files -n unifont-ttf-fonts -f %{oreon_filedir}/unifont-ttf-fonts.list
%files -n unifont-viewer -f %{oreon_filedir}/unifont-viewer.list

%changelog

%autochangelog
