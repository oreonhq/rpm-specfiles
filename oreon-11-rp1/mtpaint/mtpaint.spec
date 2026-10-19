%global source1_hash b2456ab3280923352a897e89e17b219db5a1038a623e5e2a1689a8f1e1703932
%global source0_hash 695cea10c428a8f122ed59beee5ffa49dcdcba8d88a4790eaf3c64fd7c73d6ac
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Summary:        Painting program for creating icons and pixel-based artwork
Name:          mtpaint
Version:       3.50
Release:        19%{?dist}
License:       GPL-3.0-or-later
URL:           http://mtpaint.sourceforge.net/
Source0:        http://downloads.sf.net/mtpaint/mtpaint-%{version}.tar.bz2
Source1:       http://downloads.sf.net/mtpaint/mtpaint_handbook-%{version}.zip
Patch0:        mtpaint-3.50-xdg-open.patch
Patch1:        mtpaint-3.31-png.patch
Patch2:        mtpaint-3.40-strip.patch
Patch3:        mtpaint-3.40-yad.patch
Patch4:        mtpaint-configure-c99.patch
Patch5:        mtpaint-3.50-exp10.patch
Patch6:        mtpaint-3.50-decl.patch
Requires:      ImageMagick
Requires:      /usr/bin/yad
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  giflib-devel
BuildRequires:  gtk3-devel
BuildRequires:  lcms2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  openjpeg2-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description 
mtPaint is a simple painting program designed for creating icons and
pixel-based artwork. It can edit indexed palette or 24 bit RGB images
and offers basic painting and palette manipulation tools. Its main
file format is PNG, although it can also handle JPEG, GIF, TIFF, BMP,
XPM, and XBM files.

%package       handbook
Summary:       Handbook for the mtpaint painting application
License:       GFDL-1.2-or-later
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch
%description   handbook
Install this package is want to read the handbook for the painting
application mtpaint.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -a 1
chmod 0755 mtpaint_handbook-%{version}/docs/{en_GB,img,files,cs}
dos2unix -k mtpaint_handbook-%{version}/docs/index.html
dos2unix -k mtpaint_handbook-%{version}/docs/{en_GB,cs}/*.html

%build

export CFLAGS="%{optflags} -fPIC -fcommon -Wno-incompatible-pointer-types"
export LDFLAGS="%{?__global_ldflags} -fPIC"
./configure \
    --prefix=%{_prefix} \
    --docdir=%{_pkgdocdir} \
    cflags asneeded intl man thread gtk3 GIF tiff jpeg jp2v2 imagick lcms2
make %{?_smp_mflags}
%install
make install MT_PREFIX=%{buildroot}%{_prefix}            \
             MT_MAN_DEST=%{buildroot}%{_mandir}          \
             MT_LANG_DEST=%{buildroot}%{_datadir}/locale \
             MT_DATAROOT=%{buildroot}%{_datadir}         \
             BIN_INSTALL=%{buildroot}%{_bindir}
desktop-file-install --delete-original         \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: mtpaint-devel@lists.sourceforge.net
SentUpstream: 2014-09-22
-->
<application>
  <id type="desktop">mtpaint.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Create pixel art</summary>
  <description>
    <p>
      MTPaint is an application for creating images, with a specific focus on pixel art. It features a wide range
      of tools to help you create pixel art, including: a pixel-perfect grid, tools to make pixel gradients with
      the use of dithering, pixel brushes, and pixel line and shape tools.
    </p>
  </description>
  <url type="homepage">http://mtpaint.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/mtpaint/a.png</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mtpaint-handbook -f %{oreon_filedir}/mtpaint-handbook.list

%changelog

%autochangelog
